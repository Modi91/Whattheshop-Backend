from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    )
from .serializers import (
    UserCreateSerializer,
    CategoryListSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    )

from .models import Product ,Category

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class CategoryListView(ListAPIView):
    queryset= Category.objects.all()
    serializer_class= CategoryListSerializer

class ProductListView(ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductDetailSerializer
    lookup_field= 'id'
    lookup_url_kwarg= 'product_id'