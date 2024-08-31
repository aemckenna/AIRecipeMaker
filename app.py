from flask import Flask, render_template, request
import openai
import re

# Set OpenAI API key
openai.api_key = "sk--ygmOsjWiF5YF7PDdBk_U-mvaapEI37eZgXkEblZRmT3BlbkFJ9zdJc0XJEnjPFwXPQOtDQ5pSp87cDIk-ZBx3KQpr8A"

app = Flask(__name__)

def sanitize_input(user_input):
    # Remove any special characters or numbers that could trigger the safety system
    user_input = re.sub(r'[^\w\s,]', '', user_input)
    
    # Optionally, replace any problematic words (e.g., sensitive terms)
    prohibited_words = ["word1", "word2"]  # Add any additional words to this list
    for word in prohibited_words:
        user_input = re.sub(rf'\b{word}\b', '[REDACTED]', user_input, flags=re.IGNORECASE)
    
    return user_input.strip()

@app.route("/")
def index():
    # Render form page
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_recipe():
    try:
        # Get all ingredients from the form
        ingredients_list = request.form.getlist("ingredients")
        ingredients = ", ".join(ingredients_list)

        # Sanitize the ingredients
        sanitized_ingredients = sanitize_input(ingredients)

        # Generate recipe using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a recipe assistant that helps create recipes based on ingredients provided."},
                {"role": "user", "content": f"I have {sanitized_ingredients}. What can I make?"}
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
        image_prompt = f"An appetizing dish made with {sanitized_ingredients}. The dish looks delicious and well-presented."
        image_response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )

        image_url = image_response['data'][0]['url']

        return f"<p>Recipe: {recipe}</p><img src='{image_url}' alt='Generated Image'>"

    except openai.error.InvalidRequestError as e:
        return f"<p>There was an issue generating the recipe or image: {str(e)}</p>"

if __name__ == "__main__":
    app.run(debug=True)