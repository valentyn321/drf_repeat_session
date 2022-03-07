from dataclasses import fields
from pyexpat import model
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
        ]
