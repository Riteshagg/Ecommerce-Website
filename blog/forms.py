from django import forms 
from .models import Product
  
class List(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['name', 'image','description','price','category']
      