from django.forms import fields
from store.models import product
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"