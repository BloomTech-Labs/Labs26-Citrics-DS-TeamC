import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    # weather_json
    # return weather_json

if __name__ == '__main__':
    uvicorn.run(app)