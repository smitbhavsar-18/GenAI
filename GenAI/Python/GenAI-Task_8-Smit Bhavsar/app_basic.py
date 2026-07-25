#Task-1 : basic Streamlit app
import streamlit as st

st.title("welcome to Streamlit")

name = st.text_input("Enter your name", key="name")

if st.button("Greet Me"):
    st.write(f"Hello, {name}!")