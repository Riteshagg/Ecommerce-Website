from django import forms 
from .models import Product
from .models import ProQuantity
  
class List(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['name', 'image','description','price','quantity','farmer_id','productCate_id']


class Quentity(forms.ModelForm):
    class Meta: 
        model = ProQuantity 
        fields = ['quantity_total']       
      