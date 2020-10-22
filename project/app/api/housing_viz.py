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

@router.post('/housing_viz/')
async def housing_viz(user_queried_citystates: list):
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

        # Create Boolean Statements to Avoid Errors with output
        if list_length == 1:
            state1 = user_queried_citystates[0]
            if state1 == 'New York City, NY':
                state1 = 'New York, NY'
            query1 = 'SELECT * FROM housing WHERE "city_state" IN (%(state1)s)'
            subsetH = pd.read_sql(sql = query1, columns = "city_state", params={"state1":state1}, con=engine, parse_dates=['created_at', 'updated_at'])
        elif list_length == 2:
            state1 = user_queried_citystates[0]
            state2 = user_queried_citystates[1]
            if (state1 == 'New York City, NY'):
                state1 = 'New York, NY'
            elif (state2 == 'New York City, NY'):
                state2 = 'New York, NY'
            query2 = 'SELECT * FROM housing WHERE "city_state" IN (%(state1)s, %(state2)s)'
            subsetH = pd.read_sql(sql = query2, columns = "city_state", params={"state1":state1, "state2":state2}, con=engine, parse_dates=['created_at', 'updated_at'])
        elif list_length == 3:
            state1 = user_queried_citystates[0]
            state2 = user_queried_citystates[1]
            state3 = user_queried_citystates[2]
            if (state1 == 'New York City, NY'):
                state1 = 'New York, NY'
            elif (state2 == 'New York City, NY'):
                state2 = 'New York, NY'
            elif (state3 == 'New York City, NY'):
                state3 = 'New York, NY'
            query3 = 'SELECT * FROM housing WHERE "city_state" IN (%(state1)s, %(state2)s, %(state3)s)'
            subsetH = pd.read_sql(sql = query3, columns = "city_state", params={"state1":state1, "state2":state2, "state3":state3}, con=engine, parse_dates=['created_at', 'updated_at'])
        else:
            raise Exception("Please pass a list of 1-3 City-States")

        # print(subsetH.head())
        # params=(user_queried_citystates[0], user_queried_citystates[1], user_queried_citystates[2])
        # GROUP covid data based on month and city
        # grpW = covid.groupby(['month'], as_index=False).mean()

        # Set subset of grouped df for only these city-states
        # subsetH = covid.groupby('postal', as_index=False)

        return subsetH

    subsetH = sql_query(user_queried_citystates)
    # print(subsetH.columns)
    # subsetH['deaths_percent'] = (subsetH['deaths'] / subsetH['pop']) * 100
    # subsetH['tested_percent'] = (subsetH['tested'] / subsetH['pop']) * 100
    # subsetH['positive_percent'] = (subsetH['positive'] / subsetH['pop']) * 100
    # create line chart with color var as the postal
    subsetH = subsetH.replace({'New York, NY': 'New York City, NY'}, regex=True)
    subsetH['City, State'] = subsetH['city_state']
    subsetH = subsetH.sort_values('date')
    fig = px.line(subsetH, x='date', y='value', labels={'value': r"Price ($)", 'date': 'Date'}, color='City, State', title='Average Single Family Residential/Co-op/Condo Housing Value').for_each_trace(lambda t: t.update(name=t.name.split("=")[-1]))

    # Update Layout to move legend above plot
    fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1),
                    xaxis = dict(
                      tickmode = 'array',
                      tick0 = 1,
                      dtick = 1,
                      tickvals = [1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020],
                      ticktext = ['1996', '1998', '2000', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016', '2018', '2020']
                  ))   # legend above graph top right
    fig.write_image("fig1.png")       # check image for debug
    housing_json = fig.to_json()    # save figure to JSON object to pass to WEB
    
    return housing_json
