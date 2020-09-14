from flask import Blueprint, jsonify, request, redirect, render_template
import json
from pdb import set_trace as st
from os.path import join as join_path
import pandas as pd
import numpy as np
# from web_app.ml_models.StrainRecommendation import StrainRecommendation as SR

# Extra imports if neeeded
# from flask_migrate import Migrate
# from sqlalchemy import create_engine
# import psycopg2 as psy
# from psycopg2.extras import execute_values
# from dotenv import load_dotenv
# load_dotenv()
# migrate = Migrate()
# DATABASE_URL = os.getenv(DATABASE_URL, default="try_again")

# creates blueprint object from this file
home_routes = Blueprint("home_routes", __name__)

# # columns from DF that will be used in the ML model
# df_cols = ['Ammonia', 'Apple', 'Apricot', 'Berry', 'Blue Cheese', 'Blueberry', 'Cheese', 'Chemical', 'Chestnut', 'Citrus', 'Coffee', 'Diesel', 'Earthly', 'Flowery', 'Grape', 'Grapefruit', 'Honey', 'Lavender', 'Lemon', 'Lime', 'Mango', 'Mint', 'Nutty', 'Orange', 'Pepper', 'Pine', 'Pineapple', 'Plum', 'Pungent',
        #    'Sage', 'Skunk', 'Spicy/Herbal', 'Strawberry', 'Sweet', 'Tar', 'Tea', 'Tobacco', 'Tree Fruit', 'Tropical', 'Vanilla', 'Woody', 'Aroused', 'Creative', 'Energetic', 'Euphoric', 'Focused', 'Giggly', 'Happy', 'Hungry', 'Relaxed', 'Sleepy', 'Talkative', 'Tingly', 'Uplifted', 'Hybrid', 'Indica', 'Sativa']

# Creates a route redirecting to github
@home_routes.route("/")
def github():
    '''
    Re-directs to github
    '''
    # github_url = 'https://github.com/Lambda-School-Labs/Labs26-Citrics-DS-TeamC'
    return render_template('github_button.html')

# route for weather (pre-data)
@home_routes.route("/weather")
def create_weather_json():
    '''
    Opens file, converts ot .json object and returns it
    '''
    # TODO: if this doesnt run, add 'project' before 'app' in open
    with open(join_path('db', 'weather.json')) as f:
        data = json.load(f)
    return jsonify(data)


# @home_routes.route("/web_layout_strains")
# def four_col_format():
#     '''
#     Creates new .json object with 4 columns:
#     name, desc, flavor, effect
#     '''
#     with open(join_path('web_app', 'db', 'web_layout_strains.json')) as f:
#         data = json.load(f)
#     return jsonify(data)


# def input_encoder(input_dict, df_cols):
#     """
#     Takes in a dictionary of flavors and effects and a list of dataframe features.
#     Returns the input as a one-hot encoded list
#     """
#     # Convert dictionary values for both flavors and effects to a single list
#     input_list = [val for sublist in input_dict for val in input_dict[sublist]]
#     # create a list of 0's with the same length as the dataframe features
#     one_hot_inputs = [0] * len(df_cols)
#     # Loop through list of features. If the feature is in our list of inputs,
#     # assign the corresponding index in the one_hot_input list a value of 1.
#     for i in range(len(df_cols)):
#         if df_cols[i] in input_list:
#             one_hot_inputs[i] = 1
#     return np.array(one_hot_inputs)
#     # print(input_encoder(inputs, df_cols))


# # POST: backend gives us the input .json object
# # GET: backend requests the .json output (recommendations) from ML model 
# @home_routes.route("/model", methods=["POST"])
# def final_output():
#     '''
#     Gets input data, feeds it to model, takes model output (df), converts to .json object and returns it
#     '''

#     # request .json from backend via their POST request
#     input_json_obj = request.json

#     # Run input encoder function on input .json object to get one-hot-encoded inputs for model
#     encoded_input = input_encoder(input_json_obj, df_cols)

#     # instantiates the Model Class
#     model = SR()
#     # Use method knn_predict from Model Class to predict one-hot-encoded input
#     prediction_df = model.knn_predict(encoded_input)
#     # transform df into dict, but make sure to orient=records so format is correct
#     prediction_dict = prediction_df.to_dict(orient="records")

#     # jsonify the dict so that backend/frontend can use it
#     return jsonify(prediction_dict)


# BELOW IS CODE FOR DUMMY INPUTS & OUTPUTS TO MAKE SURE ROUTES FUNCTION PROPERLY
#-------------------------------------------------------------------------------
# @home_routes.route("/dummy_model", methods=["POST", "GET"])
# def dummy_final_output():
#     '''
#     returns a dummy output json
#     '''
#     # data = request.form["data_2"]
#     # st()
#     dummy_decoded_output = [
#         {
#             "Name": "Agent Tangie",
#             "Description": "Agent Tangie is a ...",
#             "Flavors": [
#                 "Cirtus",
#                 "Diesel",
#                 "Earthy"
#             ],
#             "Effects": [
#                 "Energetic",
#                 "Focused",
#                 "Giggly"
#             ]
#         }, {
#             "Name": "Name 2",
#             "Description": "Name 2 is a ...",
#             "Flavors": [
#                 "flavor1",
#                 "flavor2",
#                 "flavor3"
#             ],
#             "Effects": [
#                 "effects1",
#                 "effects2",
#                 "effects3"
#             ]
#         }, {
#             "Name": "Name 3",
#             "Description": "Name 3 is a ...",
#             "Flavors": [
#                 "flavor1",
#                 "flavor2",
#                 "flavor3"
#             ],
#             "Effects": [
#                 "effects1",
#                 "effects2",
#                 "effects3"
#             ]
#         }
#     ]
#     # st()
#     return jsonify(dummy_decoded_output)


# # TEST METHODS
# @home_routes.route("/dummy_model_TEST", methods=["GET"])
# def dummy_final_output_TEST(df):
#     '''
#     converts a dataframe to a json object
#     '''
#     # df = pd.DataFrame(dummy_decoded_output)
#     return jsonify(df.to_dict())
