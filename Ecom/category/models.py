from enum import unique
from unicodedata import category
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description= models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='image/categories', blank=True)

    class mete:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name