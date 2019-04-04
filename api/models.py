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
    img = models.ImageField(upload_to='img_Prodect', null = True)
    img2 = models.ImageField(upload_to='img_Prodect', null = True)
    img3= models.ImageField(upload_to='img_Prodect', null = True)
    categories =  models.ManyToManyField( Category, related_name='prodects')

    def __str__(self):
        return self.name


class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total= models.DecimalField(decimal_places=2,  max_digits=10, default=0)

    def __str__(self):
        return self.user.username


class OrderProduct(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderedproduct" )
    quantity= models.IntegerField()
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name="madeorder")

    
    