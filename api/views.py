from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.views import APIView
from .serializers import (
    UserCreateSerializer, 
    CategoryListSerializer,
    ProductListSerializer, 
    OrderProductSerializer, 
    ProfileUpdateSerializer,
    ImageSerializer,
    ProfileSerializer,
    OrderListSerializer,

)
from .models import (
    Product, 
    Category, 
    OrderProduct,
    Order ,
    Profile ,
    Image
)
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

import requests

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer



class OrderProductView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer



class OrderCreateView(APIView):
    def post(self, request):
        new_order, created = Order.objects.get_or_create(user=request.user, complete=False)
        response = []
        error = "There is only {} left from {}"
        for order in request.data:
            product= Product.objects.get(id=order['product'])
            qty = order['quantity']
            order_product, created=OrderProduct.objects.get_or_create(product=product, order=new_order)
            
            if created:
                if (qty > product.stock):
                    response.append(error.format(product.stock, product.name))
                    order_product.delete()
                else:
                    order_product.quantity= qty
                    product.stock -= qty
                    order_product.save()
            elif (qty > product.stock+order_product.quantity):
                    response.append(error.format(product.stock, product.name))
            else:
                product.stock += order_product.quantity - qty
                order_product.quantity = qty
                order_product.save()
            product.save()

        if len(response)>0:
            return Response({"response":response, "link": None})
        else:
            new_order.total = sum([order_product.product.price * order_product.quantity for order_product in new_order.madeorder.all()])
            new_order.complete = True
            new_order.save()

            url = "https://api.tap.company/v2/charges"

            payload = "{\"amount\":%s,\"currency\":\"SAR\",\"threeDSecure\":false,\"save_card\":false,\"description\":\"Test Description\",\"statement_descriptor\":\"Sample\",\"metadata\":{\"udf1\":\"test 1\",\"udf2\":\"test 2\"},\"reference\":{\"transaction\":\"txn_0001\",\"order\":\"ord_0001\"},\"receipt\":{\"email\":false,\"sms\":true},\"customer\":{\"first_name\":\"%s\",\"middle_name\":\"test\",\"last_name\":\"test\",\"email\":\"test@test.com\",\"phone\":{\"country_code\":\"965\",\"number\":\"50000000\"}},\"source\":{\"id\":\"src_all\"},\"post\":{\"url\":\"http://your_website.com/post_url\"},\"redirect\":{\"url\":\"http://localhost:3000\"}}"%(new_order.total, new_order.user.username)
            headers = {
                'authorization': "Bearer sk_test_XKokBfNWv6FIYuTMg5sLPjhJ",
                'content-type': "application/json"
                }

            response = requests.request("POST", url, data=payload, headers=headers)

            json_response= response.json()

            return Response({"response":[True], "link": json_response['transaction']['url']})


class ProfileUpdateView(APIView):
    def put(self, request ):
        new_data= request.data
        new_user =  new_data['user']
        new_city =  new_data['city']
        new_district =  new_data['district']
        new_zipcode =  new_data['zip_code']
        profile = Profile.objects.filter(user = self.request.user)
        serializerprofile = ProfileUpdateSerializer(data=new_data)
        if (serializerprofile.is_valid):
            profile.update(**{'city':new_city ,'district':new_district ,'zip_code':new_zipcode})
            User.objects.filter(id=profile.first().user.id).update(**new_user)
            return Response({"Updated Thank you!"}) 
        else :
            return Response({"error"})     
    
        
class ProfileView(APIView):    
    def get(self,request):
        return Response (ProfileSerializer(self.request.user.profile).data)

