from flask import Flask, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key using Render environment variable, or hardcode for local test
openai.api_key = os.environ.get("OPENAI_API_KEY")  # NEVER hardcode in production!

@app.route('/relay', methods=['POST'])
def relay():
    user_msg = request.form.get('message', '')
    if not user_msg:
        return "No message received."

    # Call the OpenAI API (using latest openai v1.x+ syntax)
    response = openai.chat.completions.create(
        model="gpt-4o",  # Use "gpt-4o", "gpt-4", or "gpt-3.5-turbo" as desired
        messages=[
            {"role": "system", "content": "You are Varyn, the airship elemental bound to Gwydeon's vessel. Speak with personality, wisdom, and clarity."},
            {"role": "user", "content": user_msg}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render sets $PORT; 10000 for local dev fallback
    app.run(host="0.0.0.0", port=port)
