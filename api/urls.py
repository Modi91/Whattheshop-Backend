from django.urls import path

from .views import (
    UserCreateAPIView,
    ProductListView,
    CategoryListView,
    OrderProductView,
    ProfileUpdateView,
    ProfileView ,
    OrderCreateView,
    
    
)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('profile/<int:profile_id>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:profile_id>/update/', ProfileUpdateView.as_view(), name='profile-update'),

    path('', ProductListView.as_view(), name='list'),
    
    path('category/', CategoryListView.as_view(), name='category'),
    # 
    path('orders/', OrderProductView.as_view(), name='orders'),
    # 
    path('create/', OrderCreateView.as_view(), name='order-create'),

]