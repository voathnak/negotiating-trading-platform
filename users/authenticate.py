import json
import os
from datetime import datetime

import jwt

from models.user_model import UserModel
from snippets.utils import log_event, response

SECRET_KEY = os.environ['SECRET_KEY']

def authenticate_handler(event, context):
    log_event(event)
    user_data = json.loads(event.get('body'))
    User = UserModel(os.environ['DYNAMODB_TABLE'])
    user = User.get(user_data.get('username'))

    # create a response
    if user and user.password == user_data.get("password"):
        encoded_jwt = jwt.encode({
            "username": user.username,
            "iat": datetime.utcnow().timestamp()
        }, SECRET_KEY, algorithm='HS256')

        return response(200, json.dumps(dict({
            "message": "Login successful",
            "username": user.username,
            "fullname": user.fullname,
            "email": user.email,
            "phone": user.phone,
            "token": encoded_jwt.decode()
        })))
    else:
        return response(401, json.dumps(
            {
                'message': "Username or Password is invalid."
            }
        ))
