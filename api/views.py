
from rest_framework.generics import CreateAPIView ,RetrieveUpdateAPIView , DestroyAPIView ,ListAPIView,RetrieveAPIView
from .serializers import (
    UserCreateSerializer,
    CategorySerializer,
    ProductCreateUpdateSerializer  ,
    UserCreateSerializer,
    ProductListSerializer,
    ProductDetailSerializer

    )
from .models import Product ,Category
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser




class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminUser,]

class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateUpdateSerializer
    # permission_classes = [IsAdminUser,]

class ProductUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
    # permission_classes = [IsAdminUser]

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
    # permission_classes = [IsAdminUser]

class ProductListView(ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductDetailSerializer
    lookup_field= 'id'
    lookup_url_kwarg= 'product_id'

