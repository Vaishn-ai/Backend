from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length = 25)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 25)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 25)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    name = models.CharField(max_length = 25)
    description = models.TextField()
    price = models.IntegerField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class ProductVarient(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    size = models.IntegerField()
    color = models.CharField(max_length= 50)
    stock = models.IntegerField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.product
