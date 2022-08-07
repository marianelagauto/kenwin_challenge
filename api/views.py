""" views """
# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get',]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderSerializer.Meta.model.objects.all()
    http_method_names = ['get', 'post',]

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderSerializer
        return OrderSerializer