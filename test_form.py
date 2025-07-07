import streamlit as st

st.title("Test BMW Form")

name = st.text_input("Name")
feedback = st.text_area("Your thoughts on our service")

if st.button("Submit"):
    st.success(f"Thank you for your feedback, {name}!")
