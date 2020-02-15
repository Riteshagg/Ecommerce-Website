from django.db import models
from django.contrib.auth.models import User
from django import forms

class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=233)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __int__(self):
        return self.id
     

class ProQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    quantity_total = models.CharField(max_length=80)
    farmerId = models.ForeignKey(Farmer,on_delete=models.CASCADE)

    def __int__(self):
        return self.id
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='blog/images')
    farmer_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=55)
    productCate_id = models.IntegerField()

    def __int__(self):
        return self.id
           







class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    quantityid = models.ForeignKey(ProQuantity, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __int__(self):
        return self.id

    
