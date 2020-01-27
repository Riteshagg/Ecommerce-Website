from django.db import models
from django import forms
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=80)
    image = models.ImageField(upload_to='blog/images')
    class Meta: 
         indexes = [
            models.Index(fields=['name', 'name']),
            models.Index(fields=['description'], name='description1'),
            models.Index(fields=['price'], name='price1'),
            models.Index(fields=['category'], name='category1'),
            models.Index(fields=['image'], name='image1'),

        ]

    def __str__(self):
        return self.category    
        
