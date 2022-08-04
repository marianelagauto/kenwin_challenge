""" views """
# from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderSerializer.Meta.model.objects.all()

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        for detail in instance.details.all():
            detail.product.restore_stock(detail.cuantity)
            detail.product.save()
        return super(OrderViewSet, self).destroy(request, pk, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderSerializer
        return OrderSerializer