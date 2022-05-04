
from django.contrib import admin
from django.urls import path
from home.views import home, about

urlpatterns = [
    path("", home, name="Ecom-home"), 
    path("about", about, name="Ecom-about")
]
