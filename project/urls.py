from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from product.views import ProductViewSet


route = routers.DefaultRouter()
route.register(r'product', ProductViewSet, basename='Produto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]