from django.urls import path

from .views import (
    UserCreateAPIView,
    ProductListView,
    ProductDetailView,
    CategoryListView,
    OrderProductView,
    OrderListView,
    ImageView,
)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('', ProductListView.as_view(), name='list'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('image/', ImageView.as_view(), name='image'),
    # 
    path('orders/', OrderProductView.as_view(), name='orders'),
    # 
    path('checkout/', OrderListView.as_view(), name='ckeckout'),

]