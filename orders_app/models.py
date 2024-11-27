from django.db import models
from customers_app.models import Customers
from products_app.models import Products
# Create your models here.

class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )
    CART_STAGE=0
    ORDER_CONFORMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=(
        (ORDER_PROCESSED,"ORDER_PROCESSED"),
        (ORDER_DELIVERED,"ORDER_DELIVERED"),
        (ORDER_REJECTED,"ORDERD_REJECTED")
        )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL, null= True,related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItems(models.Model):
    products=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name="cartitems")
    quantity=models.ImageField(default=1)
    onwer=models.ForeignKey(Orders,on_delete=models.CASCADE,related_name="added_items")
