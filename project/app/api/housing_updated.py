from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from os.path import join as join_path
import pandas as pd
import json


router = APIRouter()

@router.get('/housing_updated')
async def housing_updated_json():
    '''
    Opens housing.json file, converts to .json object and returns it
    '''
    with open(join_path('app', 'db', 'housing_updated.json')) as f:
        data_to_encode = json.load(f)

    encoded_json = jsonable_encoder(data_to_encode)

    housing_json = json.dumps(encoded_json)

    return housing_json
