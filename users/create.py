import json
import os

import boto3
import requests

from models.user_model import UserModel
import jwt
from datetime import datetime

from snippets.utils import response, log_event, check_email

SECRET_KEY = os.environ['SECRET_KEY']

def send_mail(email_address):
    return requests.post(
        "https://api.mailgun.net/v3/mail.vlim.co/messages",
        auth=("api", "cdc6155b3734354611b31621524a3900-a65173b1-08564970"),
        data={"from": "Support <noreply@mail.vlim.co>",
              "to": [email_address],
              "subject": "Hi Voathnak Lim, please verify your NEGOTIATING TRADING PLATFORM account",
              "template": "verification-email",
              "v:title": "API Documentation",
              "v:link": "https://github.com/voathnak/react-registration-login-example/settings/access"})

def lambda_handler(event, context):
    log_event(event)
    user = UserModel(os.environ['DYNAMODB_TABLE'])

    values = json.loads(event.get('body'))

    if check_email(values.get("username")):
        values.update({"email": values.get("username")})

    existing_user = user.get(values.get('username'))
    if existing_user:
        return response(409, json.dumps({"message": "Username already exists."}))

    # write the user to the database
    user.save(values)
    # create a response
    if user:
        send_mail(user.email)
        # print("##### Email sending:", send_mail(user.email))
        encoded_jwt = jwt.encode({
            "username": user.username,
            "iat": datetime.utcnow().timestamp()
        }, SECRET_KEY, algorithm='HS256')

        return response(200, json.dumps(dict({
            "token": encoded_jwt.decode()
        })))
    else:
        return response(401, json.dumps({'message': 'User registering failed'}))
