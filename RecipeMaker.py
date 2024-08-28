from flask import Flask
import openai

# Set your OpenAI API key
client = openai.OpenAI(api_key="sk--ygmOsjWiF5YF7PDdBk_U-mvaapEI37eZgXkEblZRmT3BlbkFJ9zdJc0XJEnjPFwXPQOtDQ5pSp87cDIk-ZBx3KQpr8A")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
ingredients = "rasberries"
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a recipe assistant that will make a recipe based off ingredients that the client has"},
    {"role": "user", "content": ingredients}
  ]
)