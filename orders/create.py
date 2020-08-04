import json
import os

from models.order_model import OrderModel
from models.user_model import UserModel
from snippets.utils import get_authorizer_data, log_event, response


def lambda_handler(event, context):
    log_event(event)

    data = json.loads(event.get('body'))
    order = OrderModel(os.environ['ORDER_DYNAMODB_TABLE'])
    user = UserModel(os.environ['USER_DYNAMODB_TABLE'])

    username = get_authorizer_data(event).get("username")
    user.get(username)

    data.update({"username": username})
    if data.get('type') == 'sell':
        # check if the user have enough stock balance
        stock_balance = int(user.stock_balance.get(data.get("stock"), 0))
        if stock_balance < int(data.get("quantity")):
            return response(400, json.dumps(
                {'message': "Sorry, You do not have enough security balance to place this order."}))
    elif data.get('type') == 'buy':
        # check if the user have enough cash balance
        if user.cash_balance < int(data.get("quantity"))*float(data.get('price')):
            return response(400, json.dumps(
                {'message': "Sorry, You do not have enough cash balance to place this order."}))
    else:
        return response(400, json.dumps({'message': "Incorrect Order type."}))

    # write the order to the database
    order.save(data)

    # create a response
    return response(200, json.dumps(dict(order)))
