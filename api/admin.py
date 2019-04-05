from django.contrib import admin
from .models import (
    Product,
    Category,
    Order,
    OrderProduct,
    Image
    )

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Image)
