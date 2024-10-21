from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at']
        # fields = ['image']