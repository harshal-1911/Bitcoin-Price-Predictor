import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('linear_regression_model.joblib')

st.title('Bitcoin Price Predictor')
st.write('Enter the closing prices for the past three days to predict tomorrow\'s closing price.')

# User inputs
close_day_before_yesterday = st.number_input('Closing Price Day Before Yesterday', value=90000.0)
close_yesterday = st.number_input('Closing Price Yesterday', value=91000.0)
close_today = st.number_input('Closing Price Today', value=92000.0)

if st.button('Predict Tomorrow\'s Close'):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([{
        'Close_DayBeforeYesterday': close_day_before_yesterday,
        'Close_Yesterday': close_yesterday,
        'Close_Today': close_today
    }])

    # Make prediction
    predicted_close = model.predict(input_data)[0]

    st.success(f'Predicted Tomorrow\'s Closing Price: ${predicted_close:,.2f}')
