from django.contrib import admin
from django.urls import path
from store.views import store_home

urlpatterns = [
    path("", store_home, name="Ecom-store-home"),
    path("<slug:category_slug>/", store_home, name="Ecom-store-category"),
]
