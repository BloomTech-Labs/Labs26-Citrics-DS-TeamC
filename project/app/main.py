from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, cc, population, county_city, housing, housing_updated, jobs, jobs_updated, weather, weather_updated, temp_viz, precip_viz, snow_viz, uvindex_viz, humidity_viz, wind_viz, covid, covid_viz, housing_viz, wage_goods_viz, wage_mining_viz, wage_manufacturing_viz, wage_construction_viz, wage_trade_transport_viz, wage_financial_viz, wage_business_viz, wage_edu_health_viz, wage_hospitality_viz, wage_information_viz, wage_service_viz, wage_other_viz, wage_unclassified_viz

app = FastAPI(
    title='DRIFTLY DS API',
    description='Access our DS data on US cities for job market, housing, and weather',
    version='0.7',
    docs_url='/',
)

origins = [
    "http://localhost:8080",
    ]

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(cc.router)
app.include_router(population.router)
app.include_router(county_city.router)
app.include_router(housing.router)
app.include_router(housing_updated.router)
app.include_router(jobs.router)
app.include_router(jobs_updated.router)
app.include_router(weather.router)
app.include_router(weather_updated.router)
app.include_router(covid.router)
# app.include_router(card_viz.router)
app.include_router(temp_viz.router)
app.include_router(precip_viz.router)
app.include_router(snow_viz.router)
app.include_router(uvindex_viz.router)
app.include_router(humidity_viz.router)
app.include_router(wind_viz.router)
app.include_router(covid_viz.router)
app.include_router(housing_viz.router)
app.include_router(wage_goods_viz.router)
app.include_router(wage_mining_viz.router)
app.include_router(wage_manufacturing_viz.router)
app.include_router(wage_construction_viz.router)
app.include_router(wage_trade_transport_viz.router)
app.include_router(wage_financial_viz.router)
app.include_router(wage_business_viz.router)
app.include_router(wage_edu_health_viz.router)
app.include_router(wage_hospitality_viz.router)
app.include_router(wage_information_viz.router)
app.include_router(wage_service_viz.router)
app.include_router(wage_other_viz.router)
app.include_router(wage_unclassified_viz.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)