from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home/index.html")

def about(request):
    return HttpResponse("<h1>Welcome to Project home</h1>")