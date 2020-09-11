from flask_cors import CORS
from flask import Flask
import requests
import os
import joblib
import pandas as pd 
import sklearn
import json
import jsonify
from dotenv import load_dotenv

from app.api.routes.weather_route import weather_route


def create_app():
    app= Flask(__name__)
    cors = CORS(app)



    app.register_blueprint(weather_route)
    return app




if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)