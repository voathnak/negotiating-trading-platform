import os

from models.order_model import OrderModel
from snippets.utils import response


def delete(event, context):
    order = OrderModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    order.delete(itemId)

    # create a response
    return response(204)
