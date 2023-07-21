from flask import Flask, render_template, request
import qrcode
from base64 import b64encode
from io import BytesIO


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def createQRCode():
    imageStorgae = BytesIO()
    data = request.form.get("url")
    image = qrcode.make(data)
    # saving image to memory
    image.save(imageStorgae)
    imageStorgae.seek(0)

    # converting to image to html-readable img
    img = f"data:image/png;base64,{b64encode(imageStorgae.getvalue()).decode('ascii')} "

    return render_template("index.html", data=img)


if __name__ == "__main__":
    app.run(debug=True)
