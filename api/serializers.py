from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username',]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id', 'cuantity', 'product')


class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ('user', 'get_total', 'details')

    def create(self, validated_data):
        details = validated_data.pop('details')            
        errors = {'errors': []}

        for detail in details:  
            product = detail['product']
            try: 
                product.check_stock(detail['cuantity'])
            except ValidationError as e:
                errors['errors'].append({product.description: str(e)})

        if errors['errors']:
            raise serializers.ValidationError(errors)
        else:
            order = Order.objects.create(**validated_data)
            for detail in details: 
                detail['product'].decrease_stock(detail['cuantity'])
                detail['product'].save()
                OrderDetail.objects.create(order=order, **detail)
        return order