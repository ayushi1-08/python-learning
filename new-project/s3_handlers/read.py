import json
import boto3
import os

s3 = boto3.client('s3')
bucket_name = os.environ.get('FILE_BUCKET')

def lambda_handler(event, context):
    try:
        file_name = event['queryStringParameters']['file-name']
        
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = response['Body'].read().decode('utf-8')
        
        return {
            'statusCode': 200,
            'body': file_content
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
