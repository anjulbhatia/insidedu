import scripts.apptexts as att
import streamlit as st

st.set_page_config(
    page_title="InsideDU Community",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff; /* AliceBlue */
        }
        .card {
            background-color: #ffffff; /* White */
            border-radius: 5px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .card h4 {
            margin-bottom: 10px;
            color: #000000; /* Black */
        }
        .card p {
            margin-bottom: 20px;
            color: #000000; /* Black */
        }
        .button {
            background-color: #87cefa; /* SkyBlue */
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:hover {
            background-color: white;
            color: black;
            border: 2px solid #87cefa;
        }
    </style>
""", unsafe_allow_html=True)

st.title("InsideDU Community")
st.image("images/logo_1.png")
st.markdown('<a href="https://bit.ly/InsideDU_WACommunity" target="_blank"><button class="button">Join the Community!</button></a>', unsafe_allow_html=True)
st.write("Welcome to InsideDU Community! Use the tabs to navigate through different sections.")

tabs = st.tabs(["Home", "Products", "Resources", "About"])

with tabs[0]:
    st.image("images/Brochure.png")

    st.write("### Testimonials")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/testimonials/1.png", caption="Testimonials from our 2023 batch students")
    with col2:
        st.image("images/testimonials/2.png", caption="Testimonials from our 2023 batch students")
    with col3:
        st.image("images/testimonials/3.png", caption="Testimonials from our 2023 batch students")
    
    st.write("### Contact Us")
    st.write("Email: [aunn.insidedu@gmail.com](mailto:aunn.insidedu@gmail.com)")
    st.write("Phone: +91 9873363129; +91 999949195")

with tabs[1]:
    st.write("### Products")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>Product 1</h4>
            <p>Description of Product 1</p>
            <p><s>₹1000</s> ₹800</p>
            <button class="button">Buy Now</button>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>Product 2</h4>
            <p>Description of Product 2</p>
            <p><s>₹1200</s> ₹1000</p>
            <button class="button">Buy Now</button>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
            <h4>Product 3</h4>
            <p>Description of Product 3</p>
            <p><s>₹1500</s> ₹1300</p>
            <button class="button">Buy Now</button>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>Product 4</h4>
            <p>Description of Product 4</p>
            <p><s>₹2000</s> ₹1800</p>
            <button class="button">Buy Now</button>
        </div>
        """, unsafe_allow_html=True)

with tabs[2]:
    st.write("### Resources")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h4>DU Analyser</h4>
            <p>Analyze various aspects of Delhi University.</p>
            <a href="/du_analyser" target="_self"><button class="button">Go to DU Analyser</button></a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>Eligible Courses and Colleges</h4>
            <p>Find out which courses and colleges you are eligible for.</p>
            <a href="?page=eligible_courses_colleges" target="_self"><button class="button">Go to Eligible Courses and Colleges</button></a>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
            <h4>College Comparison Tool</h4>
            <p>Compare different colleges based on various criteria.</p>
            <a href="?page=college_comparison_tool" target="_self"><button class="button">Go to College Comparison Tool</button></a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h4>Course Wise College Comparison</h4>
            <p>Compare colleges offering the same course.</p>
            <a href="?page=course_wise_college_comparison" target="_self"><button class="button">Go to Course Wise College Comparison</button></a>
        </div>
        """, unsafe_allow_html=True)

with tabs[3]:
    st.write("### About InsideDU")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<a href="https://www.instagram.com/edu.insidedu" target="_blank"><button class="button">Instagram</button></a>', unsafe_allow_html=True)
        st.markdown('<a href="https://bit.ly/InsideDU_WACommunity" target="_blank"><button class="button">Join the Community!</button></a>', unsafe_allow_html=True)
    st.write(att.bio)
