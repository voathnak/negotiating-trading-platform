import json
import os
from models.user_model import UserModel
from snippets.utils import response


def get(event, context):
    user = UserModel(os.environ['DYNAMODB_TABLE'])
    username = event.get('pathParameters').get('username')
    user.get(username)

    # create a response
    if user:
        return response(200, json.dumps(dict(user)))
    else:
        return response(204, "Record not found")

