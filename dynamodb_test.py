import boto3
import uuid

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-southeast-2"
)

table = dynamodb.Table("CustomerSupportChat")

table.put_item(
    Item={
        "user_id": "customer1",
        "message_id": str(uuid.uuid4()),
        "customer_message": "Hello AWS DynamoDB"
    }
)

print("Message Saved Successfully!")