import streamlit as st


st.header("Select box")

option = st.selectbox(
    "What is your favorite color?",
    ("Blue", "Red", "Green")
)

st.write("Your favorite color is: ", option)