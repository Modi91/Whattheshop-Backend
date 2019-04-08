from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    stock = models.IntegerField()
    categories =  models.ManyToManyField( Category, related_name='products')

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='img_Prodect', null= True)

    def __str__(self):
        return self.product.name
    

class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total= models.DecimalField(decimal_places=2,  max_digits=10, default=0)
    complete = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class OrderProduct(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderedproduct" )
    quantity= models.IntegerField(null=True)
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name="madeorder")


class Profile (models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=120, null=True)
    district = models.CharField(max_length=20, null=True)
    zip_code = models.IntegerField(max_length= 99999, null=True)
    

