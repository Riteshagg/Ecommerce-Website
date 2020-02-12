from django.db import models
from django import forms
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='blog/images')
    farmer_id = models.IntegerField()
    quantity = models.CharField(max_length=255)
    productCate_id = models.IntegerField()
    class Meta: 
         indexes = [
            models.Index(fields=['name', 'name']),
            models.Index(fields=['description'], name='description1'),
            models.Index(fields=['price'], name='price1'),
            models.Index(fields=['image'], name='image1'),
            models.Index(fields=['farmer_id'], name='farmer_id1'),
            models.Index(fields=['productCate_id'], name='productCate_id1'),
            models.Index(fields=['quantity'], name='quantity1'),

        ]

    def __str__(self):
        return self.quantity   