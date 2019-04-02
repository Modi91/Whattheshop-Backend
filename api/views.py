
from rest_framework.generics import CreateAPIView ,RetrieveUpdateAPIView , DestroyAPIView ,ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from .serializers import (
    UserCreateSerializer,
    CategorySerializer,
    ProductCreateUpdateSerializer  ,
    UserCreateSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    UserLoginSerializer

    )
from .models import Product ,Category
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request):
		my_data = request.data
		serializer = UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


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

