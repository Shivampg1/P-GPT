import google.generativeai as genai
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Directly set your API key here (not recommended for production)
genai.configure(api_key='AIzaSyDVIgZGA1nhziDM6o1IWOiS1sMXHkyoPcM')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(user_message)
    bot_reply = response.text
    return jsonify({"bot_reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
