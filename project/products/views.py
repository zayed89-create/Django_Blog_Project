from django.shortcuts import render
from .models import Product
# Create your vi
def product(request):
    return render(request,'products/product.html')
def products(request):
    return render(request,'products/products.html',{'pro':Product.objects.all()})