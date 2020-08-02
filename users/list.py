import json
import os

from models.user_model import UserModel
from snippets.utils import log_event, response


def user_list(event, context):
    log_event(event)
    # fetch all users from the database
    User = UserModel(os.environ['DYNAMODB_TABLE'])
    users = User.list()

    # create a response
    return response(200, json.dumps([dict(result) for result in users]))
