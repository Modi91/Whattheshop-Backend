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
            return Response({"response":response})
        else:
            new_order.total = sum([order_product.product.price * order_product.quantity for order_product in new_order.madeorder.all()])
            new_order.complete = True
            new_order.save()
            return Response({"response":[True]})


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

