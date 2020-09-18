from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, housing, jobs, weather

app = FastAPI(
    title='DRIFTLY DS API',
    description='Access our DS data on US cities for job market, housing, and weather',
    version='0.3',
    docs_url='/',
)

origins = [
    "http://localhost:8080",
    ]

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(housing.router)
# app.include_router(jobs.router)
app.include_router(weather.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)