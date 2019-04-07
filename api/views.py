from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from .serializers import (
    UserCreateSerializer, 
    CategoryListSerializer,
    ProductListSerializer, 
    ProductDetailSerializer,
    OrderProductSerializer, 
    ProfileUpdateSerializer,
    ProfileSerializer
)

from .models import (
    Product, 
    Category, 
    OrderProduct,
    Order ,
    Profile
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


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'


class OrderProductView(ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class OrderListView(APIView):

    def post(self, request):
        new_data= request.data
        print("this is our user", request)

        new_order = Order.objects.create(user=request.user)
        for order in new_data:
            product= Product.objects.get(id=order['product'])
            qty = order['quantity']
            OrderProduct.objects.create(product=product, quantity=qty, order=new_order)
            
            product.stock -= qty
            product.save()
        
        new_order.total = sum([order_product.product.price * order_product.quantity for order_product in new_order.madeorder.all()])
        new_order.save()

        return Response({"msg":"Thank you!"}) 


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





