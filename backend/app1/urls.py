from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (product_apiview,  productvarient_apiview, brand_apiview, category_apiview, Subcategory_apiview)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

router.register('product', product_apiview, basename='product')
router.register('varient', productvarient_apiview, basename='varient')
router.register('brand', brand_apiview, basename='brand')
router.register('category', category_apiview, basename='category')
router.register('subcategory', Subcategory_apiview, basename='subcategory')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]