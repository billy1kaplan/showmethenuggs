from app import app
from flask import render_template
import random
import time
from threading import Timer
import requests

nugg_data = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whatthenug', methods = ['GET'])
def api_nuggs():
    if nugg_data == 0:
        tasks.getNuggValue()
    return jsonify({"conversion":str(nugg_data)})

#gets the current nugget value
def getNuggValue():
    url = ''
    changeNuggValue(random.random())

def changeNuggValue(newVal):
    print(newVal)
    nugg_data = newVal

while(True):
    getNuggValue()
    time.sleep(5)
