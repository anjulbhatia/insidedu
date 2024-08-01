import streamlit as st
import pandas as pd
import sqlite3
import os
from datetime import datetime

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
<style>
.stActionButton {
  visibility: hidden;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

def check_password(username, password):
    """Verify the password using Streamlit secrets."""
    return username == st.secrets["credentials"]["username"] and password == st.secrets["credentials"]["password"]

def run_query(query):
    """Run an SQL query and return the result as a DataFrame."""
    conn = sqlite3.connect('datasets/logs/user_interactions.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def load_data():
    """Load data from the database for manipulation."""
    st.session_state.df = run_query("SELECT * FROM interactions LIMIT 100")

def recreate_database():
    """Recreate the database by running scripts.logger"""
    os.remove('datasets/logs/user_interactions.db')
    os.system('python scripts/logger.py')
    
# Set up the page
st.set_page_config(
    page_title="Admin Maintenance Page",
    page_icon="🔧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state for login and data
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

# Login page
if not st.session_state.logged_in:
    st.markdown("### Admin Maintenance Page - Login")

    st.warning("Are you sure you are at the right place?", icon="🤔")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_password(username, password):
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Incorrect username or password")

else:
    # Admin panel
    st.title("Admin Maintenance Page")
    st.markdown("### Welcome to the Admin Panel")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.df = pd.DataFrame()  # Clear the loaded data
        st.experimental_rerun()  # Refresh the page to show the login page

    # Tabs for different functionalities
    tab1, tab2, tab3 = st.tabs(["View Logs", "Query Logs", "Export/Reset Data"])

    with tab1:
        st.header("SQL Queries")
        query = st.text_area("Enter SQL Query", value="SELECT * FROM interactions LIMIT 10", height=100)

        if st.button("Execute SQL Query"):
            if query.strip():
                try:
                    result_df = run_query(query)
                    st.write("### Query Results")
                    st.dataframe(result_df, use_container_width=True)
                except Exception as e:
                    st.error(f"Error executing query: {e}")
            else:
                st.warning("Please enter a query before submitting.")

    with tab2:
        st.header("Pandas Data Manipulation")

        if st.button("Load Data for Manipulation"):
            load_data()
            st.write("### Data for Manipulation")
            st.dataframe(st.session_state.df, use_container_width=True)

        if not st.session_state.df.empty:
            # Allow Python-like commands on DataFrame
            command = st.text_area("Enter Python Code to Manipulate DataFrame", height=100, value="")

            if st.button("Run Command"):
                try:
                    # Execute the command in the context of the DataFrame
                    df = st.session_state.df
                    exec(f"result_df = {command}", globals(), locals())
                    st.write("### Command Results")
                    try:
                        st.dataframe(locals()["result_df"], use_container_width=True)
                    except:
                        st.write(locals()["result_df"], unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error executing command: {e}")
        else:
            st.warning("Please load data first before running commands.")
    
    with tab3:
        st.header("Export/Reset Data")
        if st.button("Export Data"):
            if not st.session_state.df.empty:
                export_filename = f"interactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                st.download_button(label="Download Exported Data", data=st.session_state.df.to_csv(index=False), file_name=export_filename, mime='text/csv')
                st.success(f"Data exported as {export_filename}")
            else:
                st.warning("No data available to export. Please load data first.")

        if st.button("Reset Data"):
            try:
                recreate_database()
                st.success("All data has been reset.")
                # Reload data to reflect changes
                st.session_state.df = run_query("SELECT * FROM interactions LIMIT 100")
                st.dataframe(st.session_state.df, use_container_width=True)
            except Exception as e:
                st.error(f"Error resetting data: {e}")

