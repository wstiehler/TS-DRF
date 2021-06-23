from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet


route = DefaultRouter()
route.register(r'products', ProductViewSet, basename='protucts')

urlpatterns = route.urls