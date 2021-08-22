import random
import string

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order


class AddOrders(APIView):

    def post(self, request, *args, **kwargs):
        items = request.data.get('Items')

        item_list = str(items).split(',')
        trans_id = get_random_string(8)

        for item in item_list:

            try:
                order = Order.objects.create()
                order.trans_id = trans_id
                order.item = item

                order.save()

            except Exception as e:
                return Response({
                    'status': False,
                    'Detail': str(e)
                })

        return Response({
            'status': True,
            'Detail': 'Order ' + trans_id + ' has been created ',
            'Item Count': len(item_list)
        })


def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
