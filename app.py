import streamlit as st
import datetime
import requests

# TaxiFareModel front
st.markdown('''
# **TaxiFareModel Predictor 🚕**
''')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

st.markdown('''
---
''')

st.header('Set your ride parameters 👇')

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count

# Date and time input
pickup_date = st.date_input('Pickup date', value=datetime.date(2012, 10, 6))
pickup_time = st.time_input('Pickup time', value=datetime.time(15, 30))
pickup_datetime = f"{pickup_date} {pickup_time}"

# Pickup location inputs (default to NYC for convenience)
pickup_longitude = st.number_input('Pickup Longitude', value=40.7614327)
pickup_latitude = st.number_input('Pickup Latitude', value=-73.9798156)

# Dropoff location inputs
dropoff_longitude = st.number_input('Dropoff Longitude', value=40.6413111)
dropoff_latitude = st.number_input('Dropoff Latitude', value=-73.7781391)

# Passenger count input
passenger_count = st.slider('Passenger count', min_value=1, max_value=8, value=1)

st.markdown('''
---
''')

st.subheader('Get your prediction! 💰')

# Once we have these, let's call our API in order to retrieve a prediction

# 🤔 How could we call our API ? Off course... The `requests` package 💡

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...
params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

st.write(f"Calling API with parameters: {params}")

# 3. Let's call our API using the `requests` package...
response = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
prediction = response.json()

## Finally, we can display the prediction to the user
if response.status_code == 200:
    fare = round(prediction['fare'], 2)
    st.success(f"Estimated fare: **${fare}**")
else:
    st.error(f"Error calling API: {response.status_code} - {prediction.get('detail', 'Unknown error')}")
