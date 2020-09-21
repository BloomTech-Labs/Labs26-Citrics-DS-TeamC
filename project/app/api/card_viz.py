from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import json

router = APIRouter()

@router.post('/card_viz/')
async def viz(user_queried_citystates: list):
    """
    Visualize state unemployment rate from [Federal Reserve Economic Data](https://fred.stlouisfed.org/) 📈
    
    ### Path Parameter (POST from front-end)
    list: A list of city-states the user queried in this format: ["Albany, NY", "San Francisco, CA", "Chicago, IL"]

    ### Response
    JSON string of all figures to render with [react-plotly.js](https://plotly.com/javascript/react/)
    """

    ## HOUSING data viz
    # input_list = ["Albany, NY", "San Francisco, CA", "Indianapolis, IN"]
    idx = 0
    for idx in range(len(user_queried_citystates)):
        temp = df[df['city_state']==user_queried_citystates[idx]]
        temp = temp.sort_values('date')
        fig = px.line(temp, x='date', y='value', title=temp['city_state'].iloc[0])
        # fig_json = fig.to_json
        idx += 1
        return fig.to_json

    # Return Plotly figure as JSON string
    # return fig.to_json()



  # # Validate the state code
    # statecodes = {
    #     'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 
    #     'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 
    #     'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida', 
    #     'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 
    #     'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 
    #     'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 
    #     'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 
    #     'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 
    #     'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 
    #     'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 
    #     'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 
    #     'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 
    #     'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 
    #     'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 
    #     'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 
    #     'WI': 'Wisconsin', 'WY': 'Wyoming'
    # }
    # statecode = statecode.upper()
    # if statecode not in statecodes:
    #     raise HTTPException(status_code=404, detail=f'State code {statecode} not found')

    # # Get the state's unemployment rate data from FRED
    # url = f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={statecode}UR'
    # df = pd.read_csv(url, parse_dates=['DATE'])
    # df.columns = ['Date', 'Percent']

    # # Make Plotly figure
    # statename = statecodes[statecode]
    # fig = px.line(df, x='Date', y='Percent', title=f'{statename} Unemployment Rate')
