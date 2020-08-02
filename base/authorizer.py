# Adapted from https:#docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html#api-gateway-lambda-authorizer-token-lambda-function-create
# A simple TOKEN authorizer example to demonstrate how to use an authorization token
# to allow or deny a request.In this example, the caller named 'user'is allowed to invoke
# a request if the client - supplied token value is 'allow'.The caller is not allowed to
# invoke the request if the token value is 'deny'.If the token value is 'Unauthorized',
# the function returns the 'Unauthorized' error with an HTTP status code of 401. For any
# other token value, the authorizer returns 'Error: Invalid token' as a 500 error.
import os

import jwt
from jwt import InvalidSignatureError, DecodeError

from snippets.utils import log_event

SECRET_KEY = os.environ['SECRET_KEY']

def handler(event, context):
    log_event(event)
    token = event.get("authorizationToken").replace("Bearer ", "")
    methodArn = event.get("methodArn")
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print("decoded:", decoded)

        return generateAuthResponse('user', 'Allow', methodArn, decoded)
    except DecodeError:
        print("ERROR DecodeError")
        return generateAuthResponse('user', 'Deny', methodArn)
    except Exception as e:
        print("ERROR", e)
        return "Token is invalid"


def generateAuthResponse(principalId, effect, methodArn, context=None):
    # If you need to provide additional information to your integration
    # endpoint (e.g. your Lambda Function), you can add it to `context`
    print("effect:", effect)
    policyDocument = generatePolicyDocument(effect, methodArn)

    return {
        "principalId": principalId,
        "context": context,
        "policyDocument": policyDocument
    }

def generatePolicyDocument(effect, methodArn):
    if not effect or not methodArn:
        print("effect:", effect)
        print("methodArn:", methodArn)
        return "testing"

    policyDocument = {
        "Version": '2012-10-17',
        "Statement": [{
            "Action": 'execute-api:Invoke',
            "Effect": effect,
            "Resource": "arn:aws:execute-api:us-east-1:444536552593:af8oy0xu0b/dev/*"
            # "Resource": methodArn
        }]
    }

    return policyDocument
