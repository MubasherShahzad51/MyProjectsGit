import streamlit as st
import numpy as np
import sklearn
import pickle

model_filename = 'My_Project.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction", page_icon=":heart:")

# Create the navigation bar
nav_menu = ["Home", "Contact Us", "Login"]

# Create the responsive navbar
st.markdown("""
<div style="background-color: #8b0000; padding: 10px;">
  <span style="color: white; font-weight: bold;">Heart Disease Prediction</span>
  <span style="float: right;">
    <a href="#" style="color: white; text-decoration: none; margin-right: 10px;">{}</a>
    <a href="#" style="color: white; text-decoration: none; margin-right: 10px;">{}</a>
    <a href="#" style="color: white; text-decoration: none; margin-right: 10px;">{}</a>
  </span>
</div>
""".format(*nav_menu), unsafe_allow_html=True)

# Create the home page

sex = st.selectbox('Sex', ['Female', 'Male'])
age = st.number_input('Age',  value=0.0)
smoker = st.selectbox('Smoker', ['Yes', 'No'])
cigsPerday = st.number_input('Cigarette Per Day',value=0.0)

BpMeds = st.selectbox('Blood Pressure Medication', ['Yes', 'No'])
prevelentStroke = st.selectbox('Prevelent Stroke', ['Yes', 'No'])
prevelentHyp = st.selectbox('Prevelent Hypertension', ['Yes', 'No'])

diabetes = st.selectbox('Diabetes', ['Yes', 'No'])
totChol = st.number_input('Total Cholesterol',  value=0.0)
sysBP = st.number_input('Systolic Blood Pressure',  value=0.0)
diaBP = st.number_input('Diastolic Blood Pressure',  value=0.0)
Bmi = st.number_input('Body Mass Index',  value=0.0)
heartRate = st.number_input('Heart Rate',  value=0.0)
glucose = st.number_input('Glucose',  value=0.0)




# Perform prediction on user input
if st.button('Predict'):
    input_features = [
        1 if sex == 'Male' else 0,
        age,
        1 if smoker == 'Yes' else 0,
        cigsPerday,
        1 if BpMeds == 'Yes' else 0,
        1 if prevelentStroke == 'Yes' else 0,
        1 if prevelentHyp == 'Yes' else 0,
        1 if diabetes == 'Yes' else 0,
        totChol,
        sysBP,
        diaBP,
        Bmi,
        heartRate,
        glucose,


    ]
    prediction = model.predict([input_features])
    if prediction[0] == 1:
        prediction = 'Patient will get a Heart Disease'
    else:
        prediction = 'Patient will not get a Heart Disease'
    st.write('Prediction:', prediction)
# Customize the button style for prediction
button_style = """
    <style>
    .stButton > button {
        background-color: #8B0000;
        color: white;
        font-weight: bold;
    }
    </style>
    """
st.markdown(button_style, unsafe_allow_html=True)
