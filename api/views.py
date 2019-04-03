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
)

from .models import (
    Product, 
    Category, 
    OrderProduct,
    Order
)

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

        new_order = Order.objects.create(user=request.user)
        for order in new_data:
            product= Product.objects.get(id=order['product'])
            qty = order['quantity']
            OrderProduct.objects.create(product=product, quantity=qty, order=new_order)
        
        new_order.total = sum([order_product.product.price * order_product.quantity for order_product in new_order.madeorder.all()])

        return Response({"msg":"Thank you!"})