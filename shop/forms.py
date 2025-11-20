# from django import forms
# from .models import Category, Product
#
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']
#
#
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['category', 'name', 'description', 'price']

from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the product...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price in KES'
            }),
        }
