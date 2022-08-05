from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import *
from django.contrib.auth.models import User
import json


class ProductTestCase(TestCase):
    """Test case para productos"""
    client = APIClient()

    def setUp(self):
        auriculares = Product(
            description="auriculares JBL",
            price=7890,
            stock=1)
        parlante = Product(
            description="parlante bluetooth",
            price=5600,
            stock=0)
        auriculares.save()
        parlante.save()

    def test_get_products(self):
        """Chequeo listado de productos"""
        response = self.client.get('/api/products/', format='json')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)


class OrderTestCase(TestCase):
    """Test case para ordenes"""

    def setUp(self):
        auriculares = Product(
            description="auriculares JBL",
            price=7890,
            stock=1)
        parlante = Product(
            description="parlante bluetooth",
            price=5600,
            stock=6)
        auriculares.save()
        parlante.save()

        user = User(username="invitade1")
        user2 = User(username="invitade2")
        user.save()
        user2.save()

    def test_create_order_ok(self):
        """Chequeo la creacion de una orden"""
        client = APIClient()
        user_id = User.objects.get(username="invitade1").id
        order_data = {
            "user": user_id,
            "details": [
                {
                    "id": 1,
                    "cuantity": 2,
                    "product": 2
                }
            ]
        }
        response = client.post('/api/orders/', order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'user': 1, 'get_total': 5600.0, 'details': [
                         {'id': 1, 'cuantity': 2, 'product': 2}]})

    def test_create_order_without_stock(self):
        """Chequeo la creacion de una orden para un producto que no dispone de stock"""
        client = APIClient()
        user_id = User.objects.get(username="invitade1").id
        order_data = {
            "id": 1,
            "user": user_id,
            "details": [
                {
                    "id": 2,
                    "cuantity": 2,
                    "product": 3,
                }
            ]
        }
        response = client.post('/api/orders/', order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['errors'][0], {
                         'auriculares JBL': "['El stock no es suficiente']"})
