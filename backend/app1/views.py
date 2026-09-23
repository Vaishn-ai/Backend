from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, ProductVarientSerializer, BrandSerializer, CategorySerializer, SubCategorySerializer
from .models import Product, ProductVarient, Brand, Category, SubCategory
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class product_apiview(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  

class productvarient_apiview(ModelViewSet):
    queryset = ProductVarient.objects.all()
    serializer_class = ProductVarientSerializer
    lookup_field = 'pk'

class brand_apiview(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'

class category_apiview(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class Subcategory_apiview(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'pk'
    
