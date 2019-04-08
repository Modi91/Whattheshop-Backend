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
        new_data= request.data
        print("I'm inside the create view")
        new_order, created = Order.objects.get_or_create(user=request.user, complete=False)
        response = []
        for order in new_data:
            product= Product.objects.get(id=order['product'])
            qty = order['quantity']
    
            if (qty > product.stock):
                response.append("There is only %s left from %s" % (product.stock, product.name))
            else:
                order_product, created=OrderProduct.objects.get_or_create(product=product, order=new_order)
                if created:
                    order_product.quantity= qty
                    product.stock -= qty

                else:
                    product.stock += order_product.quantity
                    order_product.quantity= qty
                    product.stock -= qty
                product.save()
                order_product.save()

        if len(response)>0:
            return Response({"response":response})
        else:
            new_order.total = sum([order_product.product.price * order_product.quantity for order_product in new_order.madeorder.all()])
            new_order.complete = True
            new_order.save()

        return Response({"response":True})


class ProfileUpdateView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

    def put(self, request , profile_id):
        new_data= request.data
        new_user =  new_data['user']
        new_profile =  new_data['profile']
        profile = Profile.objects.filter(id =profile_id)
        profile.update(**new_profile)
        User.objects.filter(id=profile.first().user.id).update(**new_user)
       
        return Response({"msg":"Thank you!"}) 
    
        
class ProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

