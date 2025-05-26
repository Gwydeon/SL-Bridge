from flask import Flask, request
import openai
import os

app = Flask(__name__)  # <-- MAKE SURE THIS IS HERE AND ABOVE ANY ROUTES
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/relay', methods=['POST'])
def relay():
    user_msg = request.form.get('message', '')
    if not user_msg:
        return "No message received."
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Varyn, the airship elemental bound to Gwydeon's vessel. Speak with personality, wisdom, and clarity."},
                {"role": "user", "content": user_msg}
            ]
        )
        text = response.choices[0].message.content.strip()
        if not text:
            text = "Varyn whispers: 'I have nothing to say.'"
        return text
    except Exception as e:
        return f"Varyn relay error: {str(e)}"
