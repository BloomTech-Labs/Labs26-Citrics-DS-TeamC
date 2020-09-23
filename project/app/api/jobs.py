from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from os.path import join as join_path
import pandas as pd
import json


router = APIRouter()

@router.get('/jobs')
async def jobs_json():
    '''
    Opens jobs.json file, converts to .json object and returns it
    '''
    with open(join_path('app', 'db', 'jobs.json')) as f:
        data_to_encode = json.load(f)

    encoded_json = jsonable_encoder(data_to_encode)

    jobs_json = json.dumps(encoded_json)

    return jobs_json