from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Varyn's airship relay is online."

@app.route('/relay', methods=['POST'])
def relay():
    msg = request.form.get('message', '')
    print(f"Received from SL: {msg}")

    if 'status' in msg.lower():
        return "“The skies are clear. Varyn awaits your command.”"
    return "“I hear you.”"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
