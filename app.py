from flask import Flask, render_template, request
import openai

# Set OpenAI API key
openai.api_key = "sk--ygmOsjWiF5YF7PDdBk_U-mvaapEI37eZgXkEblZRmT3BlbkFJ9zdJc0XJEnjPFwXPQOtDQ5pSp87cDIk-ZBx3KQpr8A"

app = Flask(__name__)

@app.route("/")
def index():
    # Render form page
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_recipe():
    # Get all ingredients from the form
    ingredients_list = request.form.getlist("ingredients")
    ingredients = ", ".join(ingredients_list)

    # Generate recipe using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a recipe assistant that will make a recipe based on ingredients that the client has."},
            {"role": "user", "content": f"I have {ingredients}. What can I make?"}
        ]
    )

    # Access response correctly
    recipe = response.choices[0].message['content']

    # Shorten recipe to fit within the prompt limit
    if len(recipe) > 900:
        recipe_summary = recipe[:900] + "..."
    else:
        recipe_summary = recipe

    # Generate image based on the summarized recipe
    image_response = openai.Image.create(
        prompt=f"A delicious dish made with {ingredients}. {recipe_summary}",
        n=1,
        size="1024x1024"
    )

    image_url = image_response['data'][0]['url']

    return f"<p>Recipe: {recipe}</p><img src='{image_url}' alt='Generated Image'>"

if __name__ == "__main__":
    app.run(debug=True)