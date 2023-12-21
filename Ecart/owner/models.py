from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category_name = models.CharField(max_length=120,unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=150,null=True )
    
    def __str__(self):
        return self.product_name    

class Carts(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True)
    options =(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status =models.CharField(max_length=120,choices=options,default="in-cart")
    qty = models.PositiveBigIntegerField(default=1)
    
    
    def __str__(self):
        return self.product.product_name
    
class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,null=True)
    options = (
    
    ("order-placed","order-placed"),
    ("dispatched","dispatched"),
    ("in-transit","in-transit"),
    ("delivered","delivered"),
    ("cancelled","cancelled")
    )
    status = models.CharField(max_length=120,choices=options,default="order-placed")
    delivery_address = models.CharField(max_length=250,null=True)

class Reviews(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)
    rating = models.PositiveIntegerField()
    
    
    
