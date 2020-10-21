# from fastapi import APIRouter, HTTPException
# import pandas as pd
# import plotly.express as px
# import json

# router = APIRouter()

# @router.post('/card_viz/')
# async def card_viz(user_queried_citystates: list):
#     """
#     ### Path Parameter (POST from front-end)
#     list: A list of city-states the user queried in this format: ["Albany, NY", "San Francisco, CA", "Chicago, IL"]

#     ### Response
#     JSON string of all figures to render with [react-plotly.js](https://plotly.com/javascript/react/)
#     """

#     # # path for housing data
#     # relative_path = r'\app\db\housing_data_final.csv'
#     # housing = pd.read_csv(relative_path)

#     # def create_housing_fig(num_city_states):
#     #     '''
#     #     Creates a figure for average housing data over time for a city_state
#     #     Input: Number of city states queried by the user
#     #     Output: fig.to_json object
#     #     '''
#     #     index = num_city_states - 1
#     #     city_state = user_queried_citystates[index]
#     #     temp = housing[housing['city_state'] == city_state]
#     #     temp = temp.sort_values('date')
#     #     fig = px.line(temp, x='date', y='value', title=f"{temp['city_state'].iloc[0]} Real Estate Value over Time")
#     #     fig_json = fig.to_json()
#     #     return fig_json

#     def create_weather_fig(num_city_states):
#         '''
#         Creates a figure for weather data over time for a city_state
#         Input: Number of city states queried by the user
#         Output: fig.to_json object
#         '''
#         index = num_city_states - 1
#         city_state = user_queried_citystates[index]
#         temp = weather[weather['city_state'] == city_state]
#         temp = temp.sort_values('date')
#         fig = px.line(temp, x='date', y='MaxTempF', title=f"{temp['city_state'].iloc[0]} Maximum Temp (u'\N{DEGREE SIGN}'F) over Time")
#         fig_json = fig.to_json()
#         return fig_json
#     if len(user_queried_citystates) == 1:
#         fig1 = create_housing_fig(num_city_states=1)
#         return fig1
#     elif len(user_queried_citystates) == 2:
#         fig1 = create_housing_fig(num_city_states=1)
#         fig2 = create_housing_fig(num_city_states=2)
#         return fig1, fig2
#     elif len(user_queried_citystates) == 3:
#         fig1 = create_housing_fig(num_city_states=1)
#         fig2 = create_housing_fig(num_city_states=2)
#         fig3 = create_housing_fig(num_city_states=3)
#         return fig1, fig2, fig3
#     else:
#         return {}
