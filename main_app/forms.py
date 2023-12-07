# forms.py

from django import forms
from django.shortcuts import render

from .models import Product, Order
from .models import Category
from .models import Tag


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog.html', context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})
