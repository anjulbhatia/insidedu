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

colleges_campuses_df = pd.read_csv("datasets/Colleges_Campuses_Locations.csv")

with st.expander("See Data", False):
  st.dataframe(colleges_campuses_df, hide_index=True)

st.toast("Success", icon="✅")
