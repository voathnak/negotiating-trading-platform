import json
import os
import subprocess

import boto3
import pytest

from scripts.source import source

EVENT_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'events', 'orders/list-order-even.json')
CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'scripts', 'config.sh')

env = source(CONFIG_FILE)


@pytest.fixture()
def event(event_file=EVENT_FILE):
    """Trigger event"""
    with open(event_file) as f:
        return json.load(f)


@pytest.fixture()
def lambda_client():
    """Lambda client"""
    return boto3.client('lambda')


@pytest.fixture()
def lambda_function():
    """Return Lambda function name"""
    return '-'.join([env.get("APP_NAME"), env.get("STAGE_NAME"), env.get("VERSION_NAME"), 'listRoom'])



def test_handler(lambda_client, lambda_function, event):
    """Test handler"""
    r = lambda_client.invoke(
        FunctionName=lambda_function,
        InvocationType='RequestResponse',
        Payload=json.dumps(event).encode()
    )

    lambda_return = r.get('Payload').read()
    response = json.loads(lambda_return)
    response_body = json.loads(response.get('body'))
    first_item_keys_length = len(response_body.get('orders')[0].keys())
    assert first_item_keys_length == 14
