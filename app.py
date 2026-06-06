import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BASE_URL = "http://VPS_IP or API endpoint"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/languages")
def languages():
    try:
        res = requests.get(f"{BASE_URL}/languages")
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/translate", methods=["POST"])
def translate():

    text = request.form["text"]
    source = request.form["source"]
    target = request.form["target"]

    try:
        res = requests.post(
            f"{BASE_URL}/translate",
            json={
                "q": text,
                "source": source,
                "target": target,
                "format": "text"
            },
            timeout=10
        )

        data = res.json()
        return jsonify({
            "translatedText": data.get("translatedText", ""),
            "success": True
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })
    
if __name__ == "__main__":
    app.run(debug=True)