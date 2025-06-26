import streamlit as st
from granite_api import ask_granite
from symptoms_checker import check_symptoms

st.set_page_config(page_title="HealthAI Assistant", layout="centered")

st.title("🤖 HealthAI – Intelligent Healthcare Assistant")

user_input = st.text_input("Describe your symptoms, concerns, or medical question:")

if user_input:
    st.markdown("### 🧠 AI Response")
    granite_response = ask_granite(user_input)
    st.success(granite_response)
    
    st.markdown("### 🩺 Possible Conditions")
    suggestions = check_symptoms(user_input)
    st.write(suggestions)
