from google import genai
from dotenv import load_dotenv
import boto3
import uuid
import os

load_dotenv()

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# DynamoDB Connection
dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-southeast-2"
)

table = dynamodb.Table("CustomerSupportChat")

print("AI Customer Support Agent")
print("Type 'exit' to quit")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    prompt = f"""
You are a professional customer support agent.

Rules:
1. Be polite.
2. Be professional.
3. Keep responses under 100 words.
4. Ask follow-up questions if needed.

Customer Question:
{user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    bot_reply = response.text

    # Save Customer Message
    table.put_item(
        Item={
            "user_id": "customer1",
            "message_id": str(uuid.uuid4()),
            "role": "customer",
            "message": user_input
        }
    )

    # Save AI Reply
    table.put_item(
        Item={
            "user_id": "customer1",
            "message_id": str(uuid.uuid4()),
            "role": "agent",
            "message": bot_reply
        }
    )

    print("\nBot:", bot_reply)