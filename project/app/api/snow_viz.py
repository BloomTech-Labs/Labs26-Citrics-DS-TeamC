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

@router.post('/snow_viz/')
async def snow_viz(user_queried_citystates: list):
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
        Create a SQL query to grab only the user queried cities' data from the weather table in the DB.
        Output: subset grouped DF by month and city with only queried cities
        '''

        # get length of list of queried cities
        list_length = len(user_queried_citystates)
        
        # Create Boolean Statements to Avoid Errors with output
        if list_length == 1:
            city1 = user_queried_citystates[0]
            query1 = 'SELECT * FROM weather WHERE "City_State" IN (%(city1)s)'
            weather = pd.read_sql(sql = query1, columns = "City_State", params={"city1":city1}, con=engine, parse_dates=['created_at', 'updated_at'])
        elif list_length == 2:
            city1 = user_queried_citystates[0]
            city2 = user_queried_citystates[1]
            query2 = 'SELECT * FROM weather WHERE "City_State" IN (%(city1)s, %(city2)s)'
            weather = pd.read_sql(sql = query2, columns = "City_State", params={"city1":city1, "city2":city2}, con=engine, parse_dates=['created_at', 'updated_at'])
        elif list_length == 3:
            city1 = user_queried_citystates[0]
            city2 = user_queried_citystates[1]
            city3 = user_queried_citystates[2]
            query3 = 'SELECT * FROM weather WHERE "City_State" IN (%(city1)s, %(city2)s, %(city3)s)'
            weather = pd.read_sql(sql = query3, columns = "City_State", params={"city1":city1, "city2":city2, "city3":city3}, con=engine, parse_dates=['created_at', 'updated_at'])
        else:
            raise Exception("Please pass a list of 1-3 City_States")
        
        # print(weather.head())
        # create day, month, year columns from date_time column
        weather['date_time'] = pd.to_datetime(weather['date_time'], infer_datetime_format=True)
        weather['year'] = weather['date_time'].dt.year
        weather['month'] = weather['date_time'].dt.month
        weather['day'] = weather['date_time'].dt.day
        # params=(user_queried_citystates[0], user_queried_citystates[1], user_queried_citystates[2])
        # GROUP weather data based on month and city
        grpW = weather.groupby(['month', 'City_State'], as_index=False).mean()

        # Set subset of grouped df for only these city-states
        subsetW = grpW[grpW['City_State'].isin(user_queried_citystates)]

        return subsetW

    # call query function to get grouped frames from DB
    subsetW = sql_query(user_queried_citystates)

    # user_input = ['Albany, NY', 'Sacramento, CA', 'Austin, TX']   # user searched list of cities
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # create line chart with color var as the city-state
    fig = px.line(subsetW, x='month', y='TotalSnow_cm', 
                labels={'TotalSnow_cm': 'Average Daily Snowfall (cm)', 'month': 'Month'}, 
                color='City_State', title='Average Daily Snowfall Grouped by Month').for_each_trace(lambda t: t.update(name=t.name.split("=")[-1]))
    # fig.layout.title.Font("Balto")
    # fig.update_layout(tickmode='array',tickvals=months)
    # fig.update_layout(legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01))    # legend inside graph top left
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), # legend above graph top right
                  xaxis = dict(
                      tickmode = 'array',
                      tick0 = 1,
                      dtick = 1,
                      tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                      ticktext = months
                  ))   # ticks for every month
    fig.write_image("fig1.png")
    snow_json = fig.to_json()
    return snow_json