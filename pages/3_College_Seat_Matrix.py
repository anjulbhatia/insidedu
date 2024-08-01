import streamlit as st
import pandas as pd
import datasets.cuet_data as cuet_data
import sqlite3

def log_user_interaction(data):
    conn = sqlite3.connect('datasets/logs/user_interactions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO interactions (name, category, gender, language, domain1, domain2, domain3, domain4, general_test)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data['Name'], data['Category'], data['Gender'], data['Language'], data['Domain1'], data['Domain2'], data['Domain3'], data['Domain4'], data['GeneralTest']))
    conn.commit()
    conn.close()

# Function to clear cache automatically
def clear_cache():
    st.cache_data.clear()

# Load the eligibility data
df = pd.read_csv("datasets/Eligibility.csv")
supersheet_df = pd.read_csv("datasets/Supersheet.csv")

st.set_page_config(
    page_title="College Seat Matrix | InsideDU",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add custom CSS to hide the GitHub icon
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

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'categories' not in st.session_state:
    st.session_state.categories = ["UR", "OBC-NCL", "SC", "ST", "EWS", "Sikh", "Christian", "PwBD", "CW", "KM"]
if 'candidate_name' not in st.session_state:
    st.session_state.candidate_name = ""
if 'category' not in st.session_state:
    st.session_state.category = ""
if 'gender' not in st.session_state:
    st.session_state.gender = ""
if 'language' not in st.session_state:
    st.session_state.language = ""
if 'domain1' not in st.session_state:
    st.session_state.domain1 = ""
if 'domain2' not in st.session_state:
    st.session_state.domain2 = ""
if 'domain3' not in st.session_state:
    st.session_state.domain3 = ""
if 'domain4' not in st.session_state:
    st.session_state.domain4 = ""
if 'general_test' not in st.session_state:
    st.session_state.general_test = ""

# Stage 1: Candidate Details
if st.session_state.stage == 1:
    st.title("College Seat Matrix")
    st.markdown("### by InsideDU")
    
    st.markdown("#### Candidate Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        candidate_name = st.text_input("Enter Your Name")
    with col2:
        category = st.selectbox("Select Your Category", [""] + st.session_state.categories)
    with col3:
        gender = st.selectbox("Select Your Gender", [""] + ["Male", "Female", "Others"])
    
    if st.button('Next'):
        if candidate_name and category and gender:
            # Store candidate details in session state
            st.session_state.candidate_name = candidate_name
            st.session_state.category = category
            st.session_state.gender = gender
            
            # Move to next stage
            st.session_state.stage = 2
            clear_cache()
        else:
            st.warning("Please fill in all candidate details before proceeding.")

# Stage 2: CUET Subjects
elif st.session_state.stage == 2 and not st.session_state.form_submitted:
    st.title("College Seat Matrix")
    st.markdown("### by InsideDU")
    
    st.markdown("#### Select Your Subjects")
    st.warning("Caution: This resource is in its BETA development right now.")

    # Input selection for subjects in a 3-column layout
    col1, col2, col3 = st.columns(3)
    with col1:
        language = st.selectbox("Select Language", [""] + cuet_data.du_A)
    with col2:
        domain1 = st.selectbox("Select Domain 1", [""] + cuet_data.du_B1)
    with col3:
        domain2 = st.selectbox("Select Domain 2", [""] + cuet_data.du_B1)

    col1, col2, col3 = st.columns(3)
    with col1:
        domain3 = st.selectbox("Select Domain 3", [""] + cuet_data.du_B1 + cuet_data.du_B2)
    with col2:
        domain4 = st.selectbox("Select Domain 4", [""] + cuet_data.du_B1 + cuet_data.du_B2)    
    with col3:
        general_test = st.selectbox("Select General Test", [""] + cuet_data.du_GT)
    
    if language and (domain1 or domain2 or domain3 or domain4) or general_test:
        st.write("Please check the data before submitting 😇")

        # Display candidate and subject details
        candidate_df = pd.DataFrame([[st.session_state.candidate_name, st.session_state.category, st.session_state.gender]], 
                                    columns=['Name', 'Category', 'Gender'])
        st.dataframe(candidate_df, hide_index=True, use_container_width=True)

        subjects_df = pd.DataFrame(
            [[language, domain1, domain2, domain3, domain4, general_test]],
            columns=['Language', 'Domain 1', 'Domain 2', 'Domain 3', 'Domain 4', 'General Test']
        )
        st.dataframe(subjects_df, hide_index=True, use_container_width=True)

        if st.button("Submit"):
            # Store subject details in session state
            st.session_state.language = language
            st.session_state.domain1 = domain1
            st.session_state.domain2 = domain2
            st.session_state.domain3 = domain3
            st.session_state.domain4 = domain4
            st.session_state.general_test = general_test

            data = {
                'Name': st.session_state.candidate_name,
                'Category': st.session_state.category,
                'Gender': st.session_state.gender,
                'Language': st.session_state.language,
                'Domain1': st.session_state.domain1,
                'Domain2': st.session_state.domain2,
                'Domain3': st.session_state.domain3,
                'Domain4': st.session_state.domain4,
                'GeneralTest': st.session_state.general_test
            }
    
            # Log the interaction
            log_user_interaction(data)

            st.session_state.form_submitted = True
            st.success("Data submitted successfully!")
            if st.button("Check Eligibility"):
                st.session_state.form_submitted = True

# Stage 3: Display Results
elif st.session_state.form_submitted:
    st.title("College Seat Matrix")
    st.markdown("### by InsideDU")

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
            domain1_check = any(d for d in domainsA if d)
        elif course_row['Domain1'] in domainsA:
            domain1_check = True

        # Domain2 check
        if course_row['Domain2'] == 'No':
            domain2_check = True
        elif course_row['Domain2'] == 'Any':
            if any(d for d in domainsA if d):
                domain2_check = len([d for d in domainsA if d]) >= 2
        elif course_row['Domain2'] in domainsA:
            domain2_check = True

        # Domain3 check
        if course_row['Domain3'] == 'No':
            domain3_check = True
        elif course_row['Domain3'] == 'Any':
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
    
    # Retrieve subject details from session state
    candidate_name = st.session_state.candidate_name
    category = st.session_state.category
    gender = st.session_state.gender
    language = st.session_state.language
    domain1 = st.session_state.domain1
    domain2 = st.session_state.domain2
    domain3 = st.session_state.domain3
    domain4 = st.session_state.domain4
    general_test = st.session_state.general_test

    with st.expander("User Data"):
        candidate_df = pd.DataFrame([[st.session_state.candidate_name, st.session_state.category, st.session_state.gender]], 
                                        columns=['Name', 'Category', 'Gender'])
        st.dataframe(candidate_df, hide_index=True, use_container_width=True)

        subjects_df = pd.DataFrame(
            [[language, domain1, domain2, domain3, domain4, general_test]],
            columns=['Language', 'Domain 1', 'Domain 2', 'Domain 3', 'Domain 4', 'General Test']
        )
        st.dataframe(subjects_df, hide_index=True, use_container_width=True)

    # Check eligibility for each course
    eligible_courses = []
    for _, row in filtered_df.iterrows():
        if check_eligibility(row, language, domain1, domain2, domain3, domain4, general_test):
            eligible_courses.append(row)
    
    eligible_df = pd.DataFrame(eligible_courses)
    
    if not eligible_df.empty:
        course_codes = eligible_df['CourseCode'].tolist()

        # Filter supersheet data based on eligible course codes
        filtered_supersheet_df = supersheet_df[supersheet_df['CourseCode'].isin(course_codes)]
        
        col1, col2, col3 = st.columns(3)

        with col1:
            if gender != 'Female':
                filtered_supersheet_df = filtered_supersheet_df[filtered_supersheet_df['isGirls'] == 'No']
            else:
                show_girls_colleges = st.toggle("Show Only Women's Colleges")
                if show_girls_colleges:
                    filtered_supersheet_df = filtered_supersheet_df[filtered_supersheet_df['isGirls'] == 'Yes']
                else:
                    filtered_supersheet_df = filtered_supersheet_df
        with col2:
            show_evening_colleges = st.toggle("Show Evening Colleges")
            if not show_evening_colleges:
                filtered_supersheet_df = filtered_supersheet_df[filtered_supersheet_df['isEvening'] == 'No']

        with col3:
            if st.button("Clear Your Data", use_container_width=True):
                st.session_state.clear()
                filtered_supersheet_df = pd.DataFrame()

        if not filtered_supersheet_df.empty:
            if st.session_state.category == "UR":
                display_columns = ['College Name', 'Program', 'UR']
            elif st.session_state.category != "UR":
                display_columns = ['College Name', 'Program', 'UR', st.session_state.category]
            
            filtered_display_df = filtered_supersheet_df[display_columns]

            # Calculations
            total_combinations = int(filtered_display_df.shape[0])
            ur_seats = int(filtered_display_df['UR'].sum())
            category_seats = int(filtered_display_df[category].sum())
            unique_college_count = filtered_display_df['College Name'].nunique()
            unique_course_count = filtered_display_df['Program'].nunique()

            
            col1, col2, col3 = st.columns(3)
            with col1:
                cards_html = f"""
                    <div class="card-container">
                        <div class="card">
                            <h5>Total Combinations</h5>
                            <b>{total_combinations}</b>
                        </div>"""
            with col2:
                cards_html += f"""
                        <div class="card">
                            <h5>UR Seats</h5>
                            <b>{ur_seats}</b>
                        </div>"""
            if category != 'UR':
                with col3:
                    cards_html += f"""
                        <div class="card">
                            <h5>{category} Seats</h5>
                            <b>{category_seats}</b>
                        </div>"""
            
            # Additional statistics
            col4, col5 = st.columns(2)

            with col4:
                cards_html += f"""
                        <div class="card">
                            <h5>Eligible Colleges</h5>
                            <b>{unique_college_count}</b>
                        </div>"""
            with col5:
                cards_html += f"""
                        <div class="card">
                            <h5>Eligible Courses</h5>
                            <b>{unique_course_count}</b>
                        </div>"""
                
            cards_html += "</div>"
            st.markdown(cards_html, unsafe_allow_html=True)
            st.write("#### All Eligible Combinations:")
            filtered_display_df = filtered_supersheet_df[display_columns]
            filtered_display_df.index = range(1, len(filtered_display_df) + 1)
            st.dataframe(filtered_display_df, hide_index=False, use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                st.download_button(label="Download this file",
                               data=filtered_display_df.to_csv(), 
                               file_name=f"{candidate_name}.csv", 
                               mime="text/csv", use_container_width=True)
            
            with col2:
                #filter_btn = st.button("Filter Colleges and Courses", use_container_width=True)
                st.markdown("""
                    <style>
                    div[data-testid="stPageLink-NavLink"], .stPageLink{
                        display: inline-flex;
                        align-items: center;
                        justify-content: center;
                        text-align: center;
                        font-weight: 400;
                        border-radius: 0.5rem;
                        margin: -10px 0px;
                        padding-left: 50%;
                        line-height: 1;
                        text-decoration: none;
                        width: 100%;
                        background-color: rgb(255, 255, 255);
                        color: rgb(0, 0, 0);
                        border: 1px solid rgba(0, 0, 0, 0.2);        
                    }
                    div[data-testid="stPageLink"]:hover{
                        border: 1px solid rgba(0, 0, 0, 1);
                        background: white;
                    }
                    </style>
                """, unsafe_allow_html=True)
                st.page_link("app.py", label="Back to Home", use_container_width=True, icon="🔙")

        else:
            st.write("No matching colleges found.")
    else:
        st.write("No matching courses found.")
