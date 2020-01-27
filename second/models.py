from django.db import models


class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    detail = models.TextField()
    farmerId = models.ForeignKey(
        Farmer,on_delete=models.CASCADE)


