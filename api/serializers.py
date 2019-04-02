from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework import serializers


from .models import Product ,Category

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data
		

class CategoryListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields ='__all__'
		
class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model= Product
		fields= ['name', 'price', 'stock', ]

class ProductDetailSerializer(serializers.ModelSerializer):
	categories= CategoryListSerializer(many=True)
	class Meta:
		model= Product
		fields= [
			'name',
			'price',
			'description',
			'stock',
			'img',
			'categories'
		]

