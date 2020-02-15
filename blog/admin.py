from django.contrib import admin
# Register your models here.
from .models import Product, Transaction, ProQuantity

admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(ProQuantity)
