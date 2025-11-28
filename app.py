from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        user_message = request.json['message']
        
        # Send message to Rasa server
        rasa_response = requests.post(
            'http://localhost:5005/webhooks/rest/webhook',
            json={"sender": "user", "message": user_message},
            timeout=5  # Set timeout to 5 seconds
        )
        
        if rasa_response.status_code == 200:
            bot_replies = rasa_response.json()
            responses = [reply['text'] for reply in bot_replies if 'text' in reply]
            return jsonify({"responses": responses})
        else:
            return jsonify({"responses": ["Sorry, I'm having trouble connecting right now. Please try again."]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
