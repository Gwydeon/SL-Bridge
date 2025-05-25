from flask import Flask, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/relay', methods=['POST'])
def relay():
    user_msg = request.form.get('message', '')
    if not user_msg:
        return "No message received."
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Varyn, the airship elemental bound to Gwydeon's vessel. Speak with personality, wisdom, and clarity."},
            {"role": "user", "content": user_msg}
        ]
    )
    response = completion['choices'][0]['message']['content']
    return response
