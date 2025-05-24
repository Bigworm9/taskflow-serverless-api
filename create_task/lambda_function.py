import json
import boto3
import uuid
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TaskTable')

def lambda_handler(event, context):
    task_id = str(uuid.uuid4())
    timestamp = int(time.time())

    body = json.loads(event['body'])

    item = {
        'task_id': task_id,
        'description': body.get('description', 'No description'),
        'status': 'PENDING',
        'created_at': timestamp
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task created', 'task_id': task_id})
    }
