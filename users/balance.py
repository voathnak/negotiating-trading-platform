import json
import os
from models.user_model import UserModel
from snippets.utils import response, get_authorizer_data, log_event


def handler(event, context):
    log_event(event)
    user = UserModel(os.environ['DYNAMODB_TABLE'])
    stock_type = os.environ['STOCK_TYPE'].split(", ")
    username = get_authorizer_data(event).get("username")
    user.get(username)

    if user:
        stock_balance_template = dict(zip(stock_type, [0]*len(stock_type))) # make a template of all stock balances

        if event.get('httpMethod').lower() == 'get':
            stock_balance = stock_balance_template
            stock_balance.update(user.stock_balance)

        elif event.get('httpMethod').lower() == 'post':
            submitted_data = json.loads(event.get("body"))
            stock_balance_template.update(submitted_data.get('stock_balance'))
            user.update(username, {
                "cash_balance": float(submitted_data.get('cash_balance')),
                "stock_balance": stock_balance_template
            })
            stock_balance = dict(user).get('stock_balance')
        else:
            return response(404, {"message": "Invalid Http Method"})


        # create a response
        return response(200, json.dumps({
            "cash_balance": float(user.cash_balance),
            "stock_balance": stock_balance
        }))
    else:
        return response(204, "Record not found")
