import streamlit as st

st.set_page_config(
    page_title="AE Discovery & Comparison Assistant",
    page_icon="👥",
    layout="wide"
)

st.title("AE Discovery & Comparison Assistant")

st.write(
    "A proof-of-concept tool to help SSI officers discover and compare "
    "potentially relevant Adult Educators based on documented experience, "
    "expertise and past engagements."
)

st.info(
    "**POC Notice:** This application is a proof-of-concept. "
    "Information shown in the prototype should not be treated as an "
    "official AE engagement decision. The final decision remains with the officer."
)
