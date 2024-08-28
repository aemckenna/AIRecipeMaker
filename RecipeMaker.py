from flask import Flask,render_template,request
import openai
import os

# Set your OpenAI API key
openai.api_key = "sk--ygmOsjWiF5YF7PDdBk_U-mvaapEI37eZgXkEblZRmT3BlbkFJ9zdJc0XJEnjPFwXPQOtDQ5pSp87cDIk-ZBx3KQpr8A"

app = Flask(__name__)

@app.route("/")
def generate_recipe():
    ingredients = "raspberries"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a recipe assistant that will make a recipe based on ingredients that the client has."},
            {"role": "user", "content": f"I have {ingredients}. What can I make?"}
        ]
    )

    # Access the response correctly
    recipe = response.choices[0].message['content']

    return f"<p>Recipe: {recipe}</p>"

if __name__ == "__main__":
    app.run(debug=True)