from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from os.path import join as join_path
import pandas as pd
import json


router = APIRouter()

@router.get('/county_city')
async def county_city_json():
    '''
    Opens county_city.json file, converts to .json object and returns it
    '''
    with open(join_path('app', 'db', 'county_city.json')) as f:
        data_to_encode = json.load(f)

    encoded_json = jsonable_encoder(data_to_encode)

    county_city_json = json.dumps(encoded_json)

    return county_city_json