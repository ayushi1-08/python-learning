import json
def lambda_handler(event, context):
    orders = json.loads(event['body'])

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Orders processed successfully',
            'orders': orders
        })
    }