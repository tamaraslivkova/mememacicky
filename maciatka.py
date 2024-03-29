import os, openai, flask, logging, sqlite3
from flask import Flask, render_template, request, send_from_directory

logging.basicConfig(filename="mememacicky_output.log",level=logging.DEBUG)
app = Flask(__name__)


# --------------------
# IMAGE GENERATION
# --------------------

# AHOJ Tamka!
# ahoj emka/kamil
# ahojte kamosi

# OpenAI image generator
# Register to openAI using personal API KEY
@app.route('/result',methods=["POST"])
def generateimage():
    data = request.form
    prompt = f"""You are a realistic cat photo generator.\n Generate a picture of a {data['feel']} {data['color']} cat 
    wearing a {data['hat']} on a {data['background']} background with a {data['food']} and on the cat's right is a 
    {data['vinea']} kitten with {data['gift']} flower and on its left is a {data['coffee']}.Also include this text:{data['quote']}\n"""
    openai.api_key = os.getenv("OPENAI_KEY")
    response = openai.Image.create(
        prompt=prompt,
        model="dall-e-3",
        n=1,
        size="1024x1024",
        quality="standard",
    )
    image_url = response['data'][0]['url']
    app.logger.info(f"image generation: [Feeling: {data['feel']}, Color: {data['color']}, Food: {data['food']}], output URL: {image_url}")
    con = sqlite3.connect("mememacicky.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO images (url, prompt)
    VALUES(?,?)""", (image_url, prompt))
    con.commit()
    return render_template("result.html", img_url=image_url, feeling=data['feel'], colour=data['color'], vinea=data['vinea'], food=data['food'], background=data['background'], coffee=data['coffee'], quote=data['quote'], hat=data['hat'], gift=data['gift'])

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
@app.route("/mememacicky.jpg")
def icon():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'mememacicky.jpg')

# Start web application
if __name__ == "__main__":
    app.run(debug=True)

#ahoj tamarka tu je emka chybas nam
#ahoj emka aj mne chybate :(
#    ale zajtra uz pridem!
#    tesime sa na tebaa
#    aj ja na vaas
# Pocuvaj, chce sa ti teraz kodit?
# asi ani nie isla by som si radsej umyt vlasy
# dobre tak si chod umyt tie vlasy
# Len som to chcel vyskusat
#jasne oki tak idem teda
# ale uz sa ta nevieme dockat! XD
#ja tiez sa uz neviem dockat vas!!  <♥️<- toto je reaction emoji XD
# dobre, tak zitra, chod hore do code with me a daj stop sharing and kick out everyone
#oukej papa
# aj tebe!