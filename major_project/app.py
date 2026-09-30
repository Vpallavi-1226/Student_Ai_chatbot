# Major Project - Student AI Chatbot Advanced
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Major Project - AI Chatbot Working!</h1><p>Traffic & Student Bot</p>"

if __name__ == "__main__":
    app.run()
