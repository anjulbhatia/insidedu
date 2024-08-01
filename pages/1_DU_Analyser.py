import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="DU Analyser | InsideDU",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add custom CSS to hide the GitHub icon and style the cards
custom_css = """
<style>
.stActionButton {
  visibility: hidden;
}

.card {
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
  width: 30%;
  text-align: center;
  background-color: #f9f9f9;
  margin: 10px;
}

.card h5 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
}

.card b {
  font-size: 50px;
  font-weight: 700;
}

.card-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.title("DU Analyser")

# Load datasets
colleges_campuses_df = pd.read_csv("datasets/Colleges_Campuses_Locations.csv")
college_df = pd.read_csv("datasets/Supersheet.csv")

# Calculate statistics
total_colleges = college_df['College Name'].nunique()
unique_courses_offered = college_df['CourseCode'].nunique()
total_combinations = college_df[['College Name', 'Program']].drop_duplicates().shape[0]
is_girls_colleges = college_df[college_df['isGirls'] == 'Yes']['College Name'].nunique()
evening_colleges = college_df[college_df['isEvening'] == 'Yes']['College Name'].nunique()
nc_colleges = colleges_campuses_df[colleges_campuses_df['Campus'] == 'North Campus']['College'].nunique()
sc_colleges = colleges_campuses_df[colleges_campuses_df['Campus'] == 'South Campus']['College'].nunique()
oc_colleges = colleges_campuses_df[colleges_campuses_df['Campus'] == 'Off Campus']['College'].nunique()

# Display dashboard cards
st.header("Dashboard")

# Use markdown for custom card layout
cards_html = f"""
<div class="card-container">
    <div class="card">
        <h5>No of Colleges</h5>
        <b>{total_colleges}</b>
    </div>
    <div class="card">
        <h5>Unique Courses Offered</h5>
        <b>{unique_courses_offered}</b>
    </div>
    <div class="card">
        <h5>Total Combinations Offered</h5>
        <b>{total_combinations}</b>
    </div>
    <div class="card">
        <h5>Girls Colleges</h5>
        <b>{is_girls_colleges}</b>
    </div>
    <div class="card">
        <h5>Evening Colleges</h5>
        <b>{evening_colleges}</b>
    </div>
    <div class="card">
        <h5>North Campus Colleges</h5>
        <b>{nc_colleges}</b>
    </div>
    <div class="card">
        <h5>South Campus Colleges</h5>
        <b>{sc_colleges}</b>
    </div>
    <div class="card">
        <h5>Off Campus Colleges</h5>
        <b>{oc_colleges}</b>
    </div>
</div>
"""
st.markdown(cards_html, unsafe_allow_html=True)

# Campus Radio Select
colleges_display_radio = st.radio(
    "Select Campus",
    ["All Campuses","North Campus", "South Campus", "Off Campus"],
)

if colleges_display_radio == "North Campus":
    colleges_display_df = colleges_campuses_df[colleges_campuses_df['Campus'] == 'North Campus']
elif colleges_display_radio == "South Campus":
    colleges_display_df = colleges_campuses_df[colleges_campuses_df['Campus'] == 'South Campus']
elif colleges_display_radio == "Off Campus":
    colleges_display_df = colleges_campuses_df[colleges_campuses_df['Campus'] == 'Off Campus']
else:
    colleges_display_radio = "All Campuses"
    colleges_display_df = colleges_campuses_df

with st.expander(colleges_display_radio):
    st.dataframe(colleges_display_df, hide_index=True, use_container_width=True)

# Unique colleges list for multiselect
college_list = sorted(college_df['College Name'].unique())
selected_colleges = st.multiselect("Select Colleges", college_list, default=None)

# Filter the data based on selected colleges
filtered_df = college_df[college_df['College Name'].isin(selected_colleges)]

# Display filtered data
st.header("Filtered College Data")
st.dataframe(filtered_df[['College Name', 'Program']].drop_duplicates(), hide_index=True, use_container_width=True)