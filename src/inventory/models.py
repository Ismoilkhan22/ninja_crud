from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=1028)
    slug = models.SlugField(max_length=128, unique=True)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

