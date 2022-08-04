"""api views"""
from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
