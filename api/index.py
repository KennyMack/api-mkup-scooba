from api.entities import Locations
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route("/locations")
def summary():
    d = Locations()
    d.name = 'ABC',
    d.address = 'avc'
    d.image = 'vvv'
    return d