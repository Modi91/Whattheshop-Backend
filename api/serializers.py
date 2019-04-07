from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
	Product, 
	Category, 
	Order, 
	OrderProduct, 
    Profile,
	Image
)



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name','last_name','email']


    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        fname = validated_data['first_name']
        lname = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username , first_name=fname ,last_name=lname ,email=email)
        new_user.set_password(password)
        new_user.save()
        new_profile = Profile(user=new_user) #objects create
        new_profile.save()
        return validated_data


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username' ,'first_name','last_name','email']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()
    class Meta:
        model = Profile
        fields = ['user','city','district','zip_code']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = [
            'id',
			'name',
			'price',
			'description',
			'stock',
            'images',
			'categories'
        ]

    

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    order = OrderListSerializer()
    product = ProductListSerializer()
    class Meta:
        model = OrderProduct
        fields = [
            'product',
            'quantity',
            'order',
        ]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()
    class Meta:
        model = Profile
        fields = ['id','user','city','district','zip_code']


