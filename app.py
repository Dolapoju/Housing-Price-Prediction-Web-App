import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler

with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)
st.title("Housing Price Prediction Application")
st.write("Please describe the features of the house, in order to get a prediction on the valuation:")

col1, col2 = st.columns(2)

with col1:
    st.write("Note: Take your income and divide it by 10,000 and then input in MedInc")
    MedInc = st.number_input("Input the Income of the home owners($)", min_value=1.0, step=1.0)
    AveRooms = st.number_input("How many rooms in the House?", min_value=1.0,step=1.0)
    HouseAge = st.number_input("Age of House?", min_value=1.0,step=1.0)
 
with col2:
    AveBedrms = st.number_input("Number of Bedrooms?", min_value=1.0, step=1.0)
    Longitude = st.number_input("Longitude?", step=1.0, min_value=-124.4, max_value=-114.1)
    Latitude = st.number_input("Latitude?", step=1.0, min_value=32.5, max_value=42)


df = pd.DataFrame({
    "MedInc": [MedInc],
    "AveRooms": [AveRooms],
    "HouseAge": [HouseAge],
    "AveBedrms": [AveBedrms],
    "Longitude":[Longitude],
    "Latitude":[Latitude]

})

if st.button("Generate Price"):
    scaled_df = scaler.transform(df)
    prediction = model.predict(scaled_df)[0]
    st.success(f"House Price: $ {prediction * 100000:.2f}")

