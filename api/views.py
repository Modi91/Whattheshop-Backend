from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)

from rest_framework.views import APIView
from .serializers import (
    UserCreateSerializer, 
    CategoryListSerializer,
    ProductListSerializer, 
    OrderProductSerializer, 
    ImageSerializer
)

from .models import (
    Product, 
    Category, 
    OrderProduct,
    Order,
    Image
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


class OrderProductView(ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


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
                response.append({ product.name:"There is only %s left from %s" % (product.stock, product.name) })
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
