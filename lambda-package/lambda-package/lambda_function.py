import json
from google import genai

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Import Successful"
        })
    }
