import os, openai, flask
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


# --------------------
# IMAGE GENERATION
# --------------------

# OpenAI image generator
# Register to openAI using personal API KEY
@app.route('/result', methods=["POST"])
def generateimage():
    data = request.form
    prompt = f"""You are a cat meme generator. Using responses from a user form, generate a meme with a customized 
    cat. The user has answered the form with these responses:\n mood of the cat is {data['feel']}\n color of the cat's 
    fur is {data['color']}\n the clothes the cat is wearing are {data['top']} and {data['bottom']}\n the cat is 
    holding a {data['food']} in its paw\n the background of the generated image is {data['background']}\n and the 
    quote on the bottom of the image says: {data['quote']}\n"""
    openai.api_key = os.getenv("OPENAI_KEY")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url_1 = response['data'][0]['url']
    image_url_2 = response['data'][1]['url']
    image_url_3 = response['data'][2]['url']
    image_url_4 = response['data'][3]['url']
    return render_template("result.html", img_url_1=image_url_1, img_url_2=image_url_2, img_url_3=image_url_3, img_url_4=image_url_4)

# --------------------
# WEBPAGE RESOURCES
# --------------------

# Root file is the index.html
@app.route('/')
def welcome():
    return render_template("index.html")

# When user requests style css resource, return it from the resources folder
@app.route("/styles.css")
def style():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'styles.css')

# Start web application
if __name__ == "__main__":
    app.run(debug=True)
