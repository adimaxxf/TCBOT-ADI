from flask import Flask, request
import requests

app = Flask(__name__)

# YAHAN APNA TOKEN DAALO
BOT_TOKEN = "7976941515:AAHHcbK5-w9Os8d7R0g-HTUg4WtIyYDawp4"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Transform logic (10-character input)
def transform_input(text):
    if len(text) != 10 or any(c.upper() not in "SB" for c in text):
        return "Please send exactly 10 characters using only S or B."

    text = text.upper()
    positions = [7, 9, 5, 6, 8, 2, 3, 0, 4, 1]  # Mapping
    output = ''.join(text[i] for i in positions)
    return output

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'message' in data and 'text' in data['message']:
        chat_id = data['message']['chat']['id']
        incoming_text = data['message']['text']
        reply = transform_input(incoming_text)

        requests.post(URL, json={
            'chat_id': chat_id,
            'text': reply
        })
    return 'OK'

@app.route('/')
def home():
    return "Bot is running!"
  
