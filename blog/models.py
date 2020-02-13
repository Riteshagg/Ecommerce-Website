from django.db import models
from django import forms

class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=233)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    class Meta: 
        indexes = [
            models.Index(fields=['Fname'], name='Farmer1'),
            models.Index(fields=['state'], name='state1'),
            models.Index(fields=['country'], name='country1'),

        ]

class ProQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    quantity_total = models.CharField(max_length=80)
    farmerId = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    class Meta:
        indexes = [
            models.Index(fields=['quantity_total'], name='quantity_total1'),
            models.Index(fields=['farmerId'], name='farmerId1'),

        ]
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='blog/images')
    farmer_id = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=55)
    productCate_id = models.IntegerField()
    class Meta: 
         indexes = [
            models.Index(fields=['name'], name='name1'),
            models.Index(fields=['description'], name='description1'),
            models.Index(fields=['price'], name='price1'),
            models.Index(fields=['image'], name='image1'),
            models.Index(fields=['farmer_id'], name='farmer_id1'),
            models.Index(fields=['productCate_id'], name='productCate_id1'),
            models.Index(fields=['quantity'], name='quantity1'),

        ]

    def __str__(self):
        return self.quantity   







class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    quantityid = models.ForeignKey(ProQuantity,on_delete=models.CASCADE)
    farmerId = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    class Meta: 
        indexes = [
            models.Index(fields=['quantityid'], name='quantity_id1'),
            models.Index(fields=['farmerId'], name='farmerId2'),
            models.Index(fields=['productid'], name='product_id1'),
            models.Index(fields=['status'], name='status'),

        ]

    
