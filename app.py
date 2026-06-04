from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():

    text = request.form["text"]
    source = request.form["source"]
    target = request.form["target"]

    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }

    BASE_URL = "http://143.244.183.190"

    try:

        response = requests.post(
            f"{BASE_URL}/translate",
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        translated_text = data["translatedText"]

    except Exception as e:

        translated_text = f"Error: {str(e)}"

    return render_template(
        "index.html",
        translated_text=translated_text,
        original_text=text
    )

if __name__ == "__main__":
    app.run(debug=True)