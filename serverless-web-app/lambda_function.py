import json
import boto3

# Create a DynamoDB resource using boto3 (AWS SDK for Python)
dynamodb = boto3.resource('dynamodb')

# Reference the DynamoDB table
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    """
    This function runs every time the API is called.
    """

    # Try to get the current count from DynamoDB
    response = table.get_item(
        Key={
            'id': 'visitor_count'
        }
    )

    # If no record exists yet, start from 0
    if 'Item' not in response:
        count = 0
    else:
        count = response['Item']['count']

    # Increase the count
    count += 1

    # Save the updated count back to DynamoDB
    table.put_item(
        Item={
            'id': 'visitor_count',
            'count': count
        }
    )

    # Return response to API Gateway
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Allows browser access
        },
        'body': json.dumps({
            'visitor_count': count
        })
    }
