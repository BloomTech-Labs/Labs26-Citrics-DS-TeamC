# pull official base image
FROM python:3.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# install python dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip install plotly.express
RUN pip install sqlalchemy
RUN pip install psycopg2-binary
RUN pip install kaleido

# add app
COPY . .
