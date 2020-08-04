import json

import requests

from snippets.utils import response


def lambda_handler(event, context):


    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return response(200, json.dumps({
            "version": "0.0.1",
            "location": ip.text.replace("\n", "")
        }))
