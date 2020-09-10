from flask import Flask, render_template
import requests
import os
import joblib
import pandas as pd 
import sklearn

app= Flask(__name__)


@app.route('/')
def home():
    return "Hello!!"

@app.route("/item")
def read_weather():
    return "hello this is for weather"

@app.route("/room")
def read_room():
    return "The room is big"

@app.route("/something")
def read_something():
    return "Something needs to be here"

if __name__ == '__main__':
    app.run()
