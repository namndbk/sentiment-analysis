from flask import Flask, request, render_template
from flask import json, jsonify
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

from utils.preprocess import normalize_text

import pickle
import os


app = Flask(__name__)

model = pickle.load(open("models/modelv1/svm", "rb"))
transform = pickle.load(open("models/modelv1/transform", "rb"))

def predict(text):
    text = normalize_text(text.strip())
    if text == "" or len(text.split()) <= 5:
        return "Input must have a mininum of 5 words."
    text = transform.transform([text])
    y_pred = model.predict(text)
    return y_pred[-1]


@app.route("/", methods=["GET", "POST"])
@app.route("/predict", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        doc = request.form["document"]
        out = predict(doc)
        return render_template("index.html", document=doc, message=out.upper())
        


@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        message = {
            "message": "hello",
            "text": ""
        }
    else:
        doc = request.get_json()["text"]
        out = predict(doc)
        message = {
            "message": out.upper(),
            "text": doc
        }
    return jsonify(message)


if __name__ == '__main__':
	app.run(host="0.0.0.0")
