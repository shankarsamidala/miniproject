# shop/forms.py

from django import forms
from .models import Shoes, Signup

class ProductForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['brand', 'price', 'rating','size','color']

