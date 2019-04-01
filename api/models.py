from django.db import models

class Category (models.Model):
    """docstring for category """
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category


class Product(models.Model):
    """docstring for Prodect"""
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    img = models.ImageField(upload_to='img_Prodect', null = True)
    category =  models.ManyToManyField( Category, related_name='prodects')