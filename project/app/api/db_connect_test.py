# from dotenv import load_dotenv
# from pathlib import Path
# import os
# import pandas as pd
# import psycopg2
# from sqlalchemy import create_engine
# from sqlalchemy.types import Integer, Float, Text, String, DateTime

# # Load in environment Variables
# # env_path = Path('.') / '.env'
# load_dotenv()

# DB_FLAVOR = "postgres"
# DB_PYTHON_LIBRARY = "psycopg2"
# DB_HOST = os.getenv("DB_HOST")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_REGION = os.getenv("DB_REGION")
# DB_PORT = os.getenv("DB_PORT")
# # DB_URI = os.getenv("DB_URI")
# DB_URI = DB_FLAVOR + "+" + DB_PYTHON_LIBRARY + "://" + DB_USER + ":" + DB_PASS + "@" + DB_HOST + ":" + DB_PORT + "/" + DB_NAME
# engine = create_engine(DB_URI, echo=True)


# # table_name = 'weather'
# # weather_db.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=500,
# #             dtype={
# #                 "id": Integer,
# #                 "pop": Integer,
# #                 "City-State": String,
# #                 'MaxTempF': Float,
# #                 'FeelsLikeF': Float,
# #                 'MinTempF': Float,
# #                 'Precip_mm': Float,
# #                 'TotalSnow_cm': Float,
# #                 'UVindex': Integer,
# #                 'Humidity': Integer,
# #                 'WindSpeed_kmph': Integer,
# #                 'date_time': DateTime
# #             })
# weather = pd.read_sql(
#     "SELECT * FROM weather",
#     con=engine,
#     parse_dates=[
#         'created_at',
#         'updated_at'
#     ]
# )

# print(weather.head())




# # conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
# # cur = conn.cursor()
# # # cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR);")

# # cur.commit()

# # cur.close()

# # # SQLALCHEMY dataframe to SQL TABLE
# # engine = create_engine('')
# # table_name = "weather"
# # weather_df = pd.read_csv('../db/weather_df_final.csv')
# # # weather_df.to_sql(table_name, )