from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import json
from dotenv import load_dotenv
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Float, Text, String, DateTime

router = APIRouter()

@router.post('/covid_viz/')
async def covid_viz(user_queried_citystates: list):
    """
    ### Path Parameter (POST from front-end)
    list: A list of city-states the user queried in this format: ["Albany, NY", "San Francisco, CA", "Chicago, IL"]

    ### Response
    JSON string of all figures to render with [react-plotly.js](https://plotly.com/javascript/react/)
    """
    def create_db_uri():

        # give full path to .env
        env_path = r'.env'
        # LOAD environment variables
        load_dotenv(dotenv_path=env_path, verbose=True)
        # GET .env vars
        DB_FLAVOR = os.getenv("DB_FLAVOR")
        DB_PYTHON_LIBRARY = os.getenv("DB_PYTHON_LIBRARY")
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASS = os.getenv("DB_PASS")
        DB_PORT = os.getenv("DB_PORT")
        DB_URI = DB_FLAVOR + "+" + DB_PYTHON_LIBRARY + "://" + DB_USER + ":" + DB_PASS + "@" + DB_HOST + ":" + DB_PORT + "/" + DB_NAME
        return DB_URI
    
    DB_URI = create_db_uri()

    # CONNECTION Engine with SQLAlchemy
    engine = create_engine(DB_URI, echo=True)

    # _list = ["Albany, NY", "Sacramento, CA", "Austin, TX"]
    
    def sql_query(user_queried_citystates):
        '''
        Create a SQL query to grab only the user queried cities' data from the covid table in the DB.
        Output: subset grouped DF by month and city with only queried cities
        '''

        # get length of list of queried cities
        list_length = len(user_queried_citystates)

        # Create a list of just the postals from user queried city-states
        user_input_postals = []
        for i in range(len(user_queried_citystates)):
            user_input_postals.append(user_queried_citystates[i][-2:])

        # Create Boolean Statements to Avoid Errors with output
        if list_length == 1:
            state1 = user_input_postals[0]
            query1 = 'SELECT * FROM covid WHERE "postal" IN (%(state1)s)'
            subsetC = pd.read_sql(sql = query1, columns = "postal", params={"state1":state1}, con=engine, parse_dates=['created_at', 'updated_at'])
        elif list_length == 2:
            state1 = user_input_postals[0]
            state2 = user_input_postals[1]
            query2 = 'SELECT * FROM covid WHERE "postal" IN (%(state1)s, %(state2)s)'
            subsetC = pd.read_sql(sql = query2, columns = "postal", params={"state1":state1, "state2":state2}, con=engine, parse_dates=['created_at', 'updated_at'])
        elif list_length == 3:
            state1 = user_input_postals[0]
            state2 = user_input_postals[1]
            state3 = user_input_postals[2]
            query3 = 'SELECT * FROM covid WHERE "postal" IN (%(state1)s, %(state2)s, %(state3)s)'
            subsetC = pd.read_sql(sql = query3, columns = "postal", params={"state1":state1, "state2":state2, "state3":state3}, con=engine, parse_dates=['created_at', 'updated_at'])
        else:
            raise Exception("Please pass a list of 1-3 City-States")

        # print(subsetC.head())
        # params=(user_queried_citystates[0], user_queried_citystates[1], user_queried_citystates[2])
        # GROUP covid data based on month and city
        # grpW = covid.groupby(['month'], as_index=False).mean()

        # Set subset of grouped df for only these city-states
        # subsetC = covid.groupby('postal', as_index=False)

        return subsetC

    pop = pd.read_sql('SELECT * FROM pop_states', con=engine, parse_dates=['created_at', 'updated_at'])
    postals_dict = {'Alabama': 'AL','Alaska': 'AK','American Samoa': 'AS','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','District of Columbia': 'DC','Florida': 'FL','Georgia': 'GA','Guam': 'GU','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Northern Mariana Islands':'MP','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Puerto Rico': 'PR','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virgin Islands': 'VI','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}
    pop['postal'] = pop['State'].map(postals_dict)
    pop_dict = dict(zip(pop['postal'], pop['Pop2018']))
    subsetC = sql_query(user_queried_citystates)
    print(subsetC.head())
    # print(subsetC.columns)
    subsetC['pop'] = subsetC['postal'].map(pop_dict)
    subsetC['deaths_percent'] = (subsetC['deaths'] / subsetC['pop']) * 100
    subsetC['tested_percent'] = (subsetC['tested'] / subsetC['pop']) * 100
    subsetC['positive_percent'] = (subsetC['positive'] / subsetC['pop']) * 100
    # create line chart with color var as the postal
    subsetC['State'] = subsetC['postal']
    fig = px.line(subsetC, x='date', y='positive_percent', labels={'positive_percent': r"Tested Positive (% of State Population)", 'date': 'Date'}, color='State', title='Percentage of Persons Tested Positive over State Population').for_each_trace(lambda t: t.update(name=t.name.split("=")[-1]))

    # Update Layout to move legend above plot
    fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1))   # legend above graph top right
    fig.write_image("fig1.png")       # check image for debug
    covid_json = fig.to_json()    # save figure to JSON object to pass to WEB
    
    return covid_json
