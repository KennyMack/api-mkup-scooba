import os
from flask import Flask, render_template, json, jsonify
from api.entities import Locations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def getJsonData(file):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", file)
    data = json.load(open(json_url))
    return data

@app.route("/foods")
def foods():
    return jsonify(getJsonData("foods.json")), 200

@app.route("/musics")
def musics():
    return jsonify(getJsonData("musics.json")), 200

@app.route("/products")
def products():
    return jsonify(getJsonData("products.json")), 200

@app.route("/souvenirs")
def souvenirs():
    return jsonify(getJsonData("souvenirs.json")), 200

@app.route("/locations")
def locations():
    return jsonify(getJsonData("locations.json")), 200