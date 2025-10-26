import streamlit as st


def show_intro_page():
    st.title("Welcome to the Salary Prediction App")
    st.write("""
    This app helps you estimate your potential salary for software engineers based on multiple factors.
    """)

    st.image("software_Dev.jpg", width='stretch')
    st.markdown("---")
    st.subheader("Get started")
    st.write("Click the button below to continue to the prediction page.")

    # Button with unique key
    if st.button("➡️ Continue", key="continue_to_predict"):
        st.session_state["page"] = "predict"
