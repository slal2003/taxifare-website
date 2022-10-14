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


data_entry = f"""
date = {date_time} \n
pickup_longitude = {pickup_longitude} \n
"""


st.write(f'we got = {data_entry}  ')



with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")


df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
