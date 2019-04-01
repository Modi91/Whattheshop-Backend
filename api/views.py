from rest_framework.generics import CreateAPIView ,RetrieveUpdateAPIView , DestroyAPIView
from .serializers import (
    UserCreateSerializer,
    CategorySerializer,
    ProductCreateUpdateSerializer

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
