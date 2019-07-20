import json
from botocore.vendored import requests

def lambda_handler(event, context):
    id = event['id']
    base_url = 'http://35.170.242.186:8080/samples'

    response = requests.get(base_url + '/' + id)

    return {
        'statusCode': 200,
        'body': json.dumps('score of sample ' + id + ' is ' + response.text)
    }
