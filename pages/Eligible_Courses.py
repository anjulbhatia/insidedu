import streamlit as st
import pandas as pd
import datasets.cuet_data as cuet_data

# Load the eligibility data
df = pd.read_csv("datasets/Elig.csv")

st.title("Eligible Course Analyser")

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
stActionButton {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

# User input section
st.markdown("### by InsideDU")
st.header("Select Your Subjects")
st.warning("Caution: This resource is in it's BETA development right now.")

# Input selection for subjects
col1, col2 = st.columns(2)

with col1:
    language = st.selectbox("Select Language", [""] + cuet_data.du_A)
    domain1 = st.selectbox("Select Domain 1", [""] + cuet_data.du_B1)
    domain2 = st.selectbox("Select Domain 2", [""] + cuet_data.du_B1)
    domain3 = st.selectbox("Select Domain 3", [""] + cuet_data.du_B1 + cuet_data.du_B2)

with col2:
    domain4 = st.selectbox("Select Domain 4", [""] + cuet_data.du_B1 + cuet_data.du_B2)
    general_test = st.selectbox("Select General Test", [""] + cuet_data.du_GT)

st.write(language, domain1, domain2, domain3, domain4, general_test)
if st.button("Submit"):
    # Function to check eligibility
    def check_eligibility(course_row, language, domain1, domain2, domain3, domain4, general_test):
        # Initialize checks
        language_check = False
        domain1_check = False
        domain2_check = False
        domain3_check = False
        general_test_check = False
        
        # Create domain groups
        domainsA = [domain1, domain2]
        domainsB = [domain1, domain2, domain3, domain4]
        
        # Language check
        if course_row['Language'] == 'Any' or course_row['Language'] == language:
            language_check = True

        # Domain1 check
        if course_row['Domain1'] == 'No':
            domain1_check = True
        elif course_row['Domain1'] == 'Any':
            # Check if any domain is entered and also at least one is provided
            domain1_check = any(d for d in domainsA if d)
        elif course_row['Domain1'] in domainsB:
            domain1_check = True

        # Domain2 check
        if course_row['Domain2'] == 'No':
            domain2_check = True
        elif course_row['Domain2'] == 'Any':
            # Check if any domain is entered and at least two are provided
            if any(d for d in domainsA if d):
                domain2_check = len([d for d in domainsA if d]) >= 2
        elif course_row['Domain2'] in domainsB:
            domain2_check = True

        # Domain3 check
        if course_row['Domain3'] == 'No':
            domain3_check = True
        elif course_row['Domain3'] == 'Any':
            # Check if any domain is entered and at least three are provided
            if any(d for d in domainsB if d):
                domain3_check = len([d for d in domainsB if d]) >= 3
        elif course_row['Domain3'] in domainsB:
            domain3_check = True

        # General Test check
        if course_row['GeneralTest'] == 'No':
            general_test_check = True
        elif course_row['GeneralTest'] == 'Yes' and general_test:
            general_test_check = True
        
        
        
        # Return if all checks pass
        return (language_check and domain1_check and domain2_check and 
                domain3_check and general_test_check)

    # Filter the eligibility dataframe
    filtered_df = df.copy()
    
    # Check eligibility for each course
    eligible_courses = []
    for _, row in filtered_df.iterrows():
        if check_eligibility(row, language, domain1, domain2, domain3, domain4, general_test):
            eligible_courses.append(row)
    
    eligible_df = pd.DataFrame(eligible_courses)
    
    # Display the results
    if not eligible_df.empty:
        st.write("### Matching Courses:")
        st.dataframe(eligible_df[['Course']], hide_index=True)
    else:
        st.write("No matching courses found.")
