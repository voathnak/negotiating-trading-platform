import json

import requests


def lambda_handler(event, context):


    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "version": "0.0.1",
            "location": ip.text.replace("\n", "")
        }),
    }
