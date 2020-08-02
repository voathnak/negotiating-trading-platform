import json
import os

from models.user_model import UserModel
from snippets.utils import log_event, response


def update(event, context):
    log_event(event)
    user = UserModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    data = json.loads(event['body'])
    user.update(itemId, data)

    # create a response
    return response(200, json.dumps(dict(user)))

