from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
chat_history = []

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data["message"]

    chat_history.append(f"Customer: {user_message}")

    prompt = "\n".join(chat_history)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    bot_reply = response.text

    chat_history.append(f"Agent: {bot_reply}")

    return jsonify({
        "reply": bot_reply
    })
if __name__ == "__main__":
    app.run(debug=True)