import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""
            # This app will provide you with taxi fare prediction


            """)

date_time = st.text_input('Enter date and time')
pickup_longitude = st.text_input('Enter pickup_longitude')
pickup_latitude = st.text_input('Enter pickup_latitude')
dropoff_longitude = st.text_input('Enter dropoff_longitude')
dropoff_latitude = st.text_input('Enter dropoff_latitude')
passenger_count = st.text_input('Passenger count')


collected_data = f"""
date = {date_time} \n
pickup_longitude = {pickup_longitude} \n
etc
"""

st.write(f'we got \n {collected_data}  ')

# fare_query =

# url = 'https://taxifare.lewagon.ai/predict'

fare = "https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2"

fare
