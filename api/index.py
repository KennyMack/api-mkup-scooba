import os
from flask import Flask, render_template, json, jsonify
from api.entities import Locations

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/locations")
def locations():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "locations.json")
    data = json.load(open(json_url))
    return jsonify(data), 200