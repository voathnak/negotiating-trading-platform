import json
import os
import re

from models.order_model import OrderModel
from models.user_model import UserModel
from snippets.presigned_url import create_presigned_url
from snippets.utils import response, log_event



def order_list(event, context):
    log_event(event)
    # fetch all orders from the database
    order_model = OrderModel(os.environ['ROOM_DYNAMODB_TABLE'])
    orders = order_model.list()

    # create a response
    return response(200, json.dumps({'orders': [dict(order) for order in orders]}))
