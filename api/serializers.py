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
		

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)
	

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')
		try:
			user_obj = User.objects.get(username=my_username)
		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination!")

		
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)

		data["token"] = token
		return data

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields ='__all__'

class ProductCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'
		
class CategoryDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model= Category
		fields= ['title',]

class ProductListSerializer(serializers.ModelSerializer):
	class Meta:
		model= Product
		fields= ['name', 'price', 'stock', ]

class ProductDetailSerializer(serializers.ModelSerializer):
	categories= CategoryDetailSerializer(many=True)
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

