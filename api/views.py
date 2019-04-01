from rest_framework.generics import CreateAPIView
from .serializers import (
    UserCreateSerializer,
    ProductListSerializer,
    ProductDetailSerializer
    )
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from .models import (
    Product,
    Category,
)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProductListView(ListAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductListSerializer

class ProductDetailView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductDetailSerializer
    lookup_field= 'id'
    lookup_url_kwarg= 'product_id'