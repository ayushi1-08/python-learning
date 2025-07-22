import json
import boto3
import os
import uuid
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
bucket_name = os.environ.get('FILE_BUCKET')
table_name = os.environ.get('FILE_TABLE')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        file_name = event['headers']['file-name']
        file_content = event['body']
        
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        file_id = str(uuid.uuid4())
        timestamp = str(datetime.utcnow())
        
        table.put_item(
            Item={
                'id': file_id,
                'filename': file_name,
                'upload_timestamp': timestamp,
                'file_size': len(file_content)
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded and metadata saved successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
