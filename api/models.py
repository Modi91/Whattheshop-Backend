from django.db import models

# from django.contrib.auth.models import User




class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title



class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    img = models.ImageField(upload_to='img_Prodect', null = True)
    img2 = models.ImageField(upload_to='img_Prodect', null = True)
    img3= models.ImageField(upload_to='img_Prodect', null = True)
    categories =  models.ManyToManyField( Category, related_name='prodects')

    def __str__(self):
        return self.name




# class Stock(models.Model):
#   """docstring for Stack"""
#   Prodect = models.ForeignKey(Prodect,on_delete=models.CASCADE,
#       related_name='orders')
#   user = models.ForeignKey(User,on_delete=models.CASCADE,
#       related_name='orders')
#   quantity = models.IntegerField()


# class Cart(models.Model):
#   """docstring for Cart"""
#   item = models.ForeignKey(Prodect,on_delete=models.CASCADE,
#       related_name='orders')
#   user = models.ForeignKey(User,on_delete=models.CASCADE,
#       related_name='orders')
#   total = models.IntegerField()

