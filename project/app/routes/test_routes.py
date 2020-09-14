# project/app/routes/test_routes.py

# from flask import Blueprint, jsonify, request
# import json
# from pdb import set_trace as st
# from os.path import join as join_path
# import pandas as pd
# import numpy as np
# # from web_app.ml_models.StrainRecommendation import StrainRecommendation as SR
# # from web_app.unittest.test_output
# import subprocess
# from os import listdir


# # creates blueprint object from this file
# test_routes = Blueprint("test_routes", __name__)

# @test_routes.route("/test")
# def unittest_output():
#     '''
#     Takes in unittest output and displays it
#     '''
#     subprocess.run(['python3', 'project/app/unittest/test_output.py'])

#     # read the output of the 
#     with open('_log_file.txt', "r") as f:
#         test_result = f.read()
#     return test_result