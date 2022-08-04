from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import *
from django.contrib.auth.models import User
import json


class ProductTestCase(TestCase):

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
        client = APIClient()
        response = client.get(
            '/api/products/',
            format='json'
        )
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result),2)

class OrderTestCase(TestCase):

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

        user = User(
            username="invitade"
        )
        user.save()

    def test_create_order(self):
        client = APIClient()

        order_data = {
            "id": 1,
            "user": 1,
            "details": [
                {
                    "id": 1,
                    "cuantity": 2,
                    "product": 1,
                }
            ]
        }
        response = client.post(
            '/api/orders/',
            order_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['errors'][0], {'auriculares JBL': "['El stock no es suficiente']"})
