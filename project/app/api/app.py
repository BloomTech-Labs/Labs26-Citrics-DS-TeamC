from flask import Flask, render_template
import requests
import os
import joblib
import pandas as pd 
import sklearn
import json
import jsonify
from dotenv import load_dotenv


app= Flask(__name__)
# weather_json = json.loads(weather_json)
@app.route('/')
def home():
    return "home"

# @app.route('/weather')
# def weather():
#     weather_json = json.dumps(weather)
#     # weather_json = json.loads(weather_json)
#     return weather_json

# @app.route("/item")
# def read_weather():
#     return "hello this is for"

# @app.route("/room")
# def read_room():
#     return "The room is big"

# @app.route("/something")
# def read_something():
#     return "Something needs to be here"

if __name__ == '__main__':
    app.run()
