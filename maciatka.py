import os, openai, flask, logging
from flask import Flask, render_template, request, send_from_directory

logging.basicConfig(filename="mememacicky_output.log",level=logging.DEBUG)
app = Flask(__name__)


# --------------------
# IMAGE GENERATION
# --------------------

# OpenAI image generator
# Register to openAI using personal API KEY
@app.route('/result',methods=["POST"])
def generateimage():
    data = request.form
    prompt = f"""You are a cat picture generator. Using responses from a user form, generate a picture with a customized 
    cat. The user has answered the form with these responses:\n the mood of the cat is {data['feel']}.\n The color of 
    the cat's fur is {data['color']}.\n The cat is holding a {data['food']} in its paw.\n It is wearing this kind of 
    hat: {data['hat']}.\nThe background of the image
    is a {data['background']}.\n"""
    openai.api_key = os.getenv("OPENAI_KEY")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    app.logger.info(f"image generation: [Feeling: {data['feel']}, Color: {data['color']}, Food: {data['food']}], output URL: '{image_url}'")
    return render_template("result.html", img_url=image_url)

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
