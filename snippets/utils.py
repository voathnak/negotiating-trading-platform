import json
import os
import re

import jwt

email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w{2,10})+$'

def get_authorizer_data(event):
    SECRET_KEY = os.environ['SECRET_KEY']
    try:
        username = event.get("requestContext").get("authorizer") or jwt.decode(
            event.get("headers").get("Authorization").replace("Bearer ", ""), SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        print("#### Error: {}".format(e))
        return response(401, json.dumps({'message': 'Invalid Token'}))
    return username


def check_email(email):
    if (re.search(email_regex, email)):
        return True
    else:
        return False


def log_event(event):
    print("#" * 100)
    event_json = json.dumps(event, indent=4, sort_keys=False)
    print("#---- event:", event_json)
    print("#" * 100)


def log_event_body(event):
    body = json.loads(event.get("body"))
    print("#" * 100)
    event_json = json.dumps(body, indent=4, sort_keys=False)
    print("#---- event-body:", event_json)
    print("#" * 100)


def response(status_code, body=None):
    return {
        'statusCode': status_code,
        'body': body,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        }
    }
