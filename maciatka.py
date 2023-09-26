import os, openai, flask
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


# --------------------
# IMAGE GENERATION
# --------------------

# OpenAI image generator
# Register to openAI using personal API KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")
# Generate image using openAI
# openai.Image.create(
#  prompt="A cute baby sea otter",
#  n=2,
#  size="1024x1024"
# )


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
