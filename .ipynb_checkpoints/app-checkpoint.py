import pickle
import pandas as pd
import streamlit as st

with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Housing Price Prediction Application")
st.write("Please describe the features of the house, in order to get a prediction on the valuation:")

col1, col2 = st.columns(2)

with col1:
    MedInc = (st.number_input("Input the Income of the home owners($)", min_value=0.0, step=10000.0))/10000
    AveRooms = st.number_input("How many rooms in the House?", min_value=0.0,step=1.0)
    HouseAge = st.number_input("Age of House?", min_value=0.0,step=1.0)

    

with col2:
    AveBedrms = st.number_input("Number of Bedrooms?", min_value=0.0, step=1.0)
    Longitude= st.number_input("Input the Longitude")
    Latitude= st.number_input("Input the Latitude")

df = pd.DataFrame({
    "MedInc": [MedInc],
    "AveRooms": [AveRooms],
    "HouseAge": [HouseAge],
    "AveBedrms": [AveBedrms],
    "Longitude":[Longitude],
    "Latitude":[Latitude]
})

if st.button("Generate Price"):
    prediction = model.predict(df)[0]
    st.success(f"House Price: $ {prediction*100000:,.2f}")
