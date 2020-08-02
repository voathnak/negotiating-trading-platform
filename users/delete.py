import os
from models.user_model import UserModel
from snippets.utils import response


def delete(event, context):
    user = UserModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    user.delete(itemId)

    # create a response
    return response(204)
