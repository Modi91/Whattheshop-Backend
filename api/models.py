from django.db import models

class Category (models.Model):
    """docstring for category """
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    """docstring for Prodect"""
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    img = models.ImageField(upload_to='img_Prodect', null = True)
    categories =  models.ManyToManyField( Category, related_name='products')

    def __str__(self):
        return self.name