import streamlit as st
import time 

st.set_page_config(page_title="BMI CALCULATOR", page_icon="⚖️",layout="centered" )
st.title("Project 9: BMI Calculator")
st.markdown(
    """Easily find out if you're underweight, normal, overweight, or obese based on your BMI"""
)
st.markdown("---")

# User input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (meters):", min_value=0.1, step=0.01)

# Calculate Button
if st.button("Calculate BMI"):
    with st.spinner("Calculating..."):
        time.sleep(1)  # Simulate a little delay
        
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # BMI category logic
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 25:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 30:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")