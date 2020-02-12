from django import forms 
from .models import Product
  
class List(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['name', 'image','description','price','quantity','farmer_id','productCate_id']
      