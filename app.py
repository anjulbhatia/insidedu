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
            box-shadow: 0 8px 8px 0 rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .card h4 {
            margin-bottom: 10px;
            color: #000000; /* Black */
            text-align: justified;
        }
        .card p {
            margin-bottom: 20px;
            color: #000000; /* Black */
        }
        .button {
            background-color: #87cefa; /* SkyBlue */
            border: none;
            color: white;
            padding: 6px 12px;
            text-align: center;
            font-weight:bold;
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
            border: 1px solid #87cefa;
        }
            
        body {
            background-color: #f0f8ff; /* AliceBlue */
        }
        .card {
            background-color: #ffffff; /* White */
            border-radius: 5px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 4px 8px 4px rgba(0, 0, 0, 0.1);
        }
        .card h4 {
            margin-bottom: 10px;
            color: #000000; /* Black */
        }
        .card p {
            margin-bottom: 10px;
            color: #000000; /* Black */
        }
        p.price {
            margin-bottom: 20px;
            color: #000000; /* Black */
            font-size: 16px;
        }
            
        p.price bold {
            font-size: 24px;
        }

        .card-active {
            background-color: #87cefa;
            color: white;    
        }

        .button {
            background-color: #87cefa; /* SkyBlue */
            border: none;
            color: white;
            padding: 5px 12px;
            text-align: center;
            text-decoration: none;
            font-weight: medium;
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
            border: 1px solid #87cefa;
        }
        .button:disabled {
            background-color: #d3d3d3; /* LightGray */
            color: white;
            cursor: not-allowed;
            border: none;
        }    
    </style>
""", unsafe_allow_html=True)

st.title("InsideDU Community")
st.logo("images/logo_1.png")
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
    col1, col2, col3 = st.columns(3)
    
    with col2:
        st.markdown("""
        <div class="card card-active">
            <h4>Personalised Preference Sheet</h4>
            <p>Get a tailored preference sheet to meet your requirements</p>
            <p class="price"><s>₹1500</s> <b>₹500</b></p>
            <a href="#"><button class="button">Buy Now</button></a>
        </div>
        """, unsafe_allow_html=True)

    with col1:
        st.markdown("""
        <div class="card">
            <h4>Guided Preference Sheet</h4>
            <p>Get a guided preference sheet of ALL colleges for 3 courses</p>
            <p class="price"><s>₹500</s> <b>₹250</b></p>
            <a href="#"><button class="button" disabled>Buy Now</button></a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h4>1:1 Preference Sheet Review</h4>
            <p>Clear your doubts regarding DU CSAS and admission process</p>
            <p class="price"><b>₹100</b></p>
            <a href="#"><button class="button" disabled>Buy Now</button></a>
        </div>
        """, unsafe_allow_html=True)
            

with tabs[2]:
    st.write("### Resources")
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
            <a href="/Eligible_Courses_Colleges" target="_self"><button class="button">Go to Eligible Courses and Colleges</button></a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card">
            <h4>College Comparison Tool</h4>
            <p>Compare different colleges based on various criteria.</p>
            <a href="/college_comparison_tool" target="_self"><button class="button">Go to College Comparison Tool</button></a>
        </div>
        """, unsafe_allow_html=True)

with tabs[3]:
    st.write("### About InsideDU")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<a href="https://www.instagram.com/edu.insidedu" target="_blank"><button class="button">Instagram</button></a>', unsafe_allow_html=True)
        st.markdown('<a href="https://bit.ly/InsideDU_WACommunity" target="_blank"><button class="button">Join the Community!</button></a>', unsafe_allow_html=True)
    st.write(att.bio)
