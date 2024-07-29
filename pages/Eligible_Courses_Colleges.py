import streamlit as st
import pandas as pd
import datasets.cuet_data as cuet_data

# Load the eligibility data
df = pd.read_csv("datasets/Eligibility.csv")

st.title("Eligible Course Analyser")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff; /* AliceBlue */
        }
    </style>
""", unsafe_allow_html=True)

# User input section
st.markdown("### by InsideDU")
st.header("Select Your Subjects")

# Inputs
languages = st.multiselect("Select Languages (1 or 2)", cuet_data.du_A)
domains = st.multiselect("Select Domains (1 to 4)", cuet_data.du_B1 + cuet_data.du_B2)
general_test = st.checkbox("Include General Test")

# Validate input
if len(languages) > 2:
    st.error("You can select up to 2 languages.")
if len(domains) > 4:
    st.error("You can select up to 4 domains.")

def check_eligibility(course_row, selected_languages, selected_domains, general_test_selected):
    # Check language requirement
    if course_row['Language'] != "Any" and course_row['Language'] not in selected_languages:
        return False

    # Check Domain1 requirement
    if course_row['Domain1'] != "No":
        if course_row['Domain1'] != "Any" and course_row['Domain1'] not in selected_domains:
            return False

    # Check Domain2 requirement
    if course_row['Domain2'] != "No":
        if course_row['Domain2'] != "Any" and course_row['Domain2'] not in selected_domains:
            return False

    # Check Domain3 requirement
    if course_row['Domain3'] != "No":
        if course_row['Domain3'] != "Any" and course_row['Domain3'] not in selected_domains:
            return False

    # Check General Test requirement
    if course_row['GeneralTest'] == "Yes" and not general_test_selected:
        return False

    return True

if st.button("Submit"):
    # Filter the eligibility dataframe
    eligible_courses = df[df.apply(lambda row: check_eligibility(row, languages, domains, general_test), axis=1)]
    
    # Display the results
    if not eligible_courses.empty:
        st.write("### Matching Courses:")
        st.dataframe(eligible_courses[['Course', 'CourseCode']])
    else:
        st.write("No matching courses found.")
