import streamlit as st
from prediction import show_predict_page
from intro import show_intro_page

if "page" not in st.session_state:
    st.session_state["page"] = "intro"

# sidbar
sidebar = st.sidebar
sidebar.header('Salary Prediction for CS majors')
sidebar.write(
    "The current salary prediction model is based on StackOverflow survey data for 2024.")

# Sidebar selectbox
option = sidebar.selectbox(
    "Navigate", ("🏠 Intro", "💲  Predict")
)
mapping = {
    "🏠 Intro": "intro",
    "💲  Predict": "predict",

}

if st.session_state["page"] != mapping[option]:
    st.session_state["page"] = mapping[option]

if st.session_state["page"] == "intro":
    show_intro_page()
elif st.session_state["page"] == "predict":
    show_predict_page()
