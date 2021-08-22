import json

from django.test import TestCase, Client
from django.urls import *
from orders.views import AddOrders


# Create your tests here.

class TestViews(TestCase):

    def setup(self):
        self.client = Client()

    def test_add_orders(self):
        url = reverse('order')
        data = '{"Items":"Shoes"}'
        response = self.client.post(url, data=json.loads(data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)["status"], True)
        self.assertEqual(json.loads(response.content)['Item Count'], 1)


class TestURLS(TestCase):
    def setup(self):
        self.client = Client()

    def test_order_url(self):
        url = reverse('order')
        view = resolve(url).func.view_class
        self.assertEqual(view, AddOrders)
