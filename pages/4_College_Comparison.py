import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="College Comparison | InsideDU",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Load the comparison dataframe
comparison_df = pd.read_csv("datasets/College_Comparison.csv")

# Define CSS for the card layout
card_css = """
<style>
.stActionButton {
  visibility: hidden;
}
.card {
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
  width: 100%;
  text-align: center;
  background-color: #f9f9f9;
  margin: 10px;
}

.card h5 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  display: flex;
  flex-wrap: wrap;
  text-align: center;
  justify-content:center;
  text-overflow: ellipsis;
}

.card b {
  font-size: 30px;
  font-weight: 700;
}

.card-container {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

@media only screen and (max-width: 600px) {
  .card-container {
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;
  }
  .card {
    width: 100%;
  }
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(card_css, unsafe_allow_html=True)

st.header("College Comparison")

with st.expander("Description and Parameters"):
    st.markdown("""
        This College Comparison tool helps you compare the top colleges of **Delhi University** based on the following parameters:\n
        - **General Perception** (15%)  
        - **Placements** (25%)  
        - **Infrastructure** (20%)   
        - **Graduate Outcome** (25%)  
        - **Student Satisfaction** (15%)
                
        #### Comparison Flow
        1. **Overall Score Comparison:**
        The primary comparison is based on the Overall Score. If one college has a higher Overall Score, it is considered better.
        
        2. **Level of Preference:**
        If the Overall Scores are the same, the Level of Preference is compared. The college with the higher Level of Preference is considered better.
        
        3. **Preference Indexing:**
        If both the Overall Score and Level of Preference are the same, the Preference Indexing is compared. The college with the higher Preference Indexing is considered better.
    """)
    st.warning('''
        **Remember**: The comparison is **objective** and college preference may differ for various courses.\n
        This is **NOT** a course-specific comparison and candidates are advised to do more research regarding the same.
    ''')

    st.warning("**Note**: Ratings and Comparisons drawn here are based on personal experience and research. \nCandidates are suggested to further research before drawing a conclusion.")

colleges = comparison_df["College"].unique()
col1, col2 = st.columns(2)

with col1:
    college1 = st.selectbox("Select a college", colleges)

with col2:
    college2 = st.selectbox("Select another college", colleges[colleges != college1])

if st.button("Compare colleges") and college1 and college2:
    college1_data = comparison_df[comparison_df["College"] == college1].iloc[0]
    college2_data = comparison_df[comparison_df["College"] == college2].iloc[0]

    college1_A_score = float(college1_data["Overall Score"])
    college2_A_score = float(college2_data["Overall Score"])

    st.subheader("Overall Score Comparison")
    col1, col2 = st.columns(2)

    # Display A_Score comparison in info messages
    with col1:
        st.info(f"{college1}: {college1_A_score}")

    with col2:
        st.info(f"{college2}: {college2_A_score}")

    if college1_A_score == college2_A_score:
        st.info("Both colleges have the same **Overall Score**.")

        # Proceed to Level of Preference comparison
        college1_preference = float(college1_data["Level of Preference"])
        college2_preference = float(college2_data["Level of Preference"])

        st.markdown("##### Tie Breaker")

        if college1_preference == college2_preference:

            st.info("Both colleges have the same **Level Of Preference**.")

            # Proceed to Perception Indexing comparison
            college1_preference_index = float(college1_data["Perception Indexing"])
            college2_preference_index = float(college2_data["Perception Indexing"])

            if college1_preference_index == college2_preference_index:
                st.info("Both colleges have the same **Perception Indexing**.")
            elif college1_preference_index > college2_preference_index:
                st.info(f"{college2} is better than {college2} based on **Perception Indexing**.")
            else:
                st.info(f"{college1} is better than {college2} based on **Perception Indexing**.")
        elif college1_preference > college2_preference:
            st.info(f"{college2} is better than {college1} based on **Level of Preference**.")
        else:
            st.info(f"{college1} is better than {college2} based on **Level of Preference**.")
    elif college1_A_score > college2_A_score:
        st.info(f"{college1} is better than {college2} based on **Overall Score**.")
    else:
        st.info(f"{college2} is better than {college1} based on **Overall Score**.")

    st.subheader("Detailed Comparison")
    col1, col2 = st.columns(2)
    # Display comparison details in expanders
    with col1:
        with st.expander(f"{college1} Details"):
            st.table(college1_data[[
                'Campus', 'General Perception (15%)', 'Placements (25%)',
                'Infrastructure (20%) ', 'Graduate Outcome (25%)', 'Student Satisfaction (15%)', 'Overall Score'
            ]])
    with col2:
        with st.expander(f"{college2} Details"):
            st.table(college2_data[[
                'Campus', 'General Perception (15%)', 'Placements (25%)',
                'Infrastructure (20%) ', 'Graduate Outcome (25%)', 'Student Satisfaction (15%)', 'Overall Score'
            ]])
