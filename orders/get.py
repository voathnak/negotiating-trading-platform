import json
import os

from models.order_model import OrderModel
from snippets.utils import response


def get(event, context):
    order = OrderModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    order.get(itemId)

    # create a response
    if order:
        return response(200, json.dumps(dict(order)))
    else:
        return response(204, "Record not found")

