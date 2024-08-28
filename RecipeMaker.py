from flask import Flask
from openai import OpenAI
client = OpenAI()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

