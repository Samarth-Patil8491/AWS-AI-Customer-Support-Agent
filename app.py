from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Store conversation history
chat_history = []

print("AI Customer Support Agent")
print("Type 'exit' to quit")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    # Save customer message
    chat_history.append(f"Customer: {user_input}")

    # Build prompt with memory
    prompt = f"""
You are a professional customer support agent.

Rules:
1. Be polite and professional.
2. Keep responses under 100 words.
3. Ask follow-up questions when needed.
4. Never invent company policies.
5. Help the customer solve their issue.
6. Use previous conversation context when replying.

Conversation History:
{chr(10).join(chat_history)}
"""

    # Send to Gemini
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        bot_reply = response.text

    except Exception as e:
        bot_reply = f"AI service error: {str(e)}"

    # Save bot response
    chat_history.append(f"Agent: {bot_reply}")

    print("\nBot:", bot_reply)