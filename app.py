import streamlit as st


import numpy as np
import pandas as pd

import datetime as dt
import requests

st.markdown("""
            # This app will provide you with taxi fare prediction


            """)

pickup_date = st.date_input('Enter pickup date', value = dt.datetime(2022,10,14,15,22,32) )
pickup_time = st.time_input('Enter pickup time', value = dt.datetime(2022,10,14,15,22,32))
pickup_longitude = st.text_input('Enter pickup_longitude', value=(40))
pickup_latitude = st.text_input('Enter pickup_latitude', value=(73))
dropoff_longitude = st.text_input('Enter dropoff_longitude', value=(41))
dropoff_latitude = st.text_input('Enter dropoff_latitude', value=(41))
passenger_count = st.text_input('Passenger count', value=(1))

pickup_datetime = f'{pickup_date} {pickup_time}'

url = 'https://taxifare.lewagon.ai/predict'

query = ('pickup_datetime=' + pickup_datetime
         + '&pickup_longitude=' + pickup_longitude
         + '&pickup_latitude=' + pickup_latitude
         + '&dropoff_longitude=' + dropoff_longitude
         + '&dropoff_latitude=' + dropoff_latitude
         + '&passenger_count=' + passenger_count
         )

fare_query_url = url + '?' + query

fare = requests.get(fare_query_url).json()
fare = fare['fare']
fare = "${: 0,.2f}".format(fare)
st.write(f'fare = {fare}')
