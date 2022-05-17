from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True)
    context_data = {
        "products" : products,
    }
    return render(request, "home/index.html", context_data)

def about(request):
    return HttpResponse("<h1>Welcome to Project home</h1>")