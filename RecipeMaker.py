from flask import Flask
import openai

# Set your OpenAI API key
client = openai.OpenAI(api_key="sk--ygmOsjWiF5YF7PDdBk_U-mvaapEI37eZgXkEblZRmT3BlbkFJ9zdJc0XJEnjPFwXPQOtDQ5pSp87cDIk-ZBx3KQpr8A")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"