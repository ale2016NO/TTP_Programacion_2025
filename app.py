from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/productos")
def productos():
    with open("static/productos.json") as f:
        return jsonify(json.load(f))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    pid = data.get("productId")
    return jsonify(prediccion=100 + len(pid) * 2)

if __name__ == "__main__":
    app.run(debug=True)