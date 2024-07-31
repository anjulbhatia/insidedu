import streamlit as st
import pandas as pd
import datasets.cuet_data as cuet_data

st.set_page_config(
    page_title="DU Analyser | InsideDU",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
<style>
.stActionButton {
  visibility: hidden;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.title("DU Analyser")
st.write("Analyze various aspects of Delhi University here.")
# Add more content and functionality as needed

# Load the College_Campuses_Location data
df = pd.read_csv("datasets/Colleges_Campuses_Locations.csv")

st.dataframe(df)