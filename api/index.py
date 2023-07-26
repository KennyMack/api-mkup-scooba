from api.entities import Locations
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route("/locations")
def locations():
    data = {'name': 'Burger king', 'address': 'rua 1', 'image': 'image 1'}
    return jsonify(data), 200
    """d = Locations(

    )
    d.name = 'ABC',
    d.address = 'avc'
    d.image = 'vvv'
    return d"""