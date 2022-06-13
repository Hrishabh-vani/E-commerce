from turtle import home
from django.contrib import admin
from django.urls import path, include

#Addind static files 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("store/", include('store.urls')),
    path("", include('home.urls')),
    path("cart/", include('carts.urls'))
]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)