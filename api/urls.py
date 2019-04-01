from django.urls import path

from .views import (
    UserCreateAPIView,
    ProductListView,
    ProductDetailView,
    ProductCreateView ,
    ProductUpdateView ,
    ProductDeleteView
)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:product_id>/update', ProductUpdateView.as_view(), name='update'),
    path('<int:product_id>/delete', ProductDeleteView.as_view(), name='delete'),

    path('', ProductListView.as_view(), name='list'),
    path('<int:product_id>', ProductDetailView.as_view(), name='detail'),

]