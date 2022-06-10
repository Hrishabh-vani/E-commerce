from django.contrib import admin
from django.urls import path
from store.views import store_home , product_detail

urlpatterns = [
    path("", store_home, name="Ecom-store-home"),
    path("<slug:category_slug>/", store_home, name="Ecom-store-category"),
    path("<slug:category_slug>/<slug:product_slug>/", product_detail , name="Ecom-product-detail")
]
