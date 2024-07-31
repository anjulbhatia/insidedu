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
        .stActionButton {
            visibility: hidden;
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

        /* Floating buttons */
    .floating-container {
        position: fixed;
        bottom: 50px;
        right: 20px;
        display: grid;
            }
    .floating-button {
        color: white;
        border: none;
        border-radius: 50%;
        padding: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        font-size: 1.5em;
        margin: 5px;
    }
    .floating-button-instagram {
        background: transparent;
        box-shadow: none;
            
    }
    .floating-button:hover {
        transform: scale(120%);
    }  
    s {
        color: maroon; font-size:16px;        
    }
    </style>
""", unsafe_allow_html=True)

st.logo("images/logo_1.png")
st.title("InsideDU Community")

tabs = st.tabs(["Home", "Products", "Resources", "About"])

with tabs[0]:
    # Title
    st.markdown('<div class="title">Inside DU Community</div>', unsafe_allow_html=True)

    # Subtitle
    st.markdown('<div class="subtitle">Bringing to you what you need the most right now</div><br>', unsafe_allow_html=True)

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
    # Instagram
    st.markdown('''
                <a class="" href="https://www.instagram.com/edu.insidedu">
                    <img 
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/2048px-Instagram_icon.png"
                        alt="Instagram" style="width:24px;height:24px;"> /edu.insidedu
                </a><br>''', unsafe_allow_html=True)

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
            <a href="/Eligible_Courses" target="_self"><button class="button">Go to Eligible Courses</button></a>
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
    # Custom CSS for styling
    st.markdown("""
        <style>
        .title {
            font-size: 2.5em;
            color: #3498db;
            text-align: center;
            margin-top: 20px;
        }
        .subtitle {
            font-size: 1.5em;
            color: #2c3e50;
            text-align: center;
            margin-top: 10px;
        }
        .features {
            display: flex;
            flex-direction: column;
            align-items: center;

        }
        .highlight {
            font-size: 1.2em;
            font-weight: 600;
            margin: 10px 0;
            padding-left: 15px;
            margin: 10px;
            background-image: linear-gradient(
                to bottom right,
                transparent 50%,
                #b393d3 50%
                ),
                linear-gradient(#b393d3, #b393d3),
                linear-gradient(to top left, transparent 50%, #b393d3 50%);
            background-repeat: no-repeat;
            background-size: 10px 40px, calc(100% - 20px) 40px, 10px 40px;
            background-position: left center, center, right;
        }

        .flex-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* Three equal columns */
            gap: 20px; /* Space between items */
            margin: 20px;
        }
        .stats {
            font-size: 1.1em;
            color: #16a085;
            margin: 10px 0;
        }
        .card {
            background-color: #f7f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 10px;
            flex: 1;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .card-title {
            font-size: 1.2em;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .card-content {
            font-size: 1em;
            color: #2c3e50;
        }
        .link {
            color: #3498db;
            text-decoration: none;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #95a5a6;
        }
        b {font-size:56px; font-weight:700;}
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="title">Inside DU Community</div>', unsafe_allow_html=True)

    # Subtitle
    st.markdown('<div class="subtitle">Bringing to you what you need the most right now</div>', unsafe_allow_html=True)

    # Features
    features = [
        "Instant doubt solving",
        "Live sessions",
        "Admission updates",
        "College & Course review",
        "Preference list review",
        "Personalised preference Sheet",
        "Career Guidance",
        "And DU ke andar ki baatein"
    ]
    st.markdown(f'''<div class="features">''', unsafe_allow_html=True)
    for feature in features:
        st.markdown(f'''<div class="highlight">{feature}</div>''', unsafe_allow_html=True)
    st.markdown(f'''</div>''', unsafe_allow_html=True)

    # Community Background
    st.markdown('<div class="subtitle">About Us</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
        <div class="card-title">A Community Built by Students</div>
        <div class="card-content">
            A community built by students from North Campus by merit and happens to be cousins by coincidence that understands your problems because we have faced them first hand. 
            Mentorship begins after the community reaches 200 members. Share with your friends who may benefit from this:
            <br><a href="https://bit.ly/InsideDU_WACommunity" class="link">Join Inside DU Community</a>.
            <br>Also support us on Instagram: <a href="https://instagram.com/edu.insidedu" class="link">instagram.com/edu.insidedu</a>
        </div>
        </div>
    """, unsafe_allow_html=True)

    # Statistics Section
    st.markdown('<br><div class="subtitle">2023-2024 Statistics</div>', unsafe_allow_html=True)
    stats = [
        "<b>200+</b><br> member community",
        "<b>10+</b><br> seniors mentoring y'all",
        "<b>150+</b><br> college converts through our personalized preference sheets",
        "<b>2</b><br> Live sessions",
        "Instant doubt resolution",
        "Career Guidance"
    ]

    st.markdown('<div class="flex-container">', unsafe_allow_html=True)
    for stat in stats:
        st.markdown(f"""
            <div class="card">
                <div class="card-title">{stat}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Success Stories Section
    st.markdown('<div class="subtitle">Our Success Stories</div>', unsafe_allow_html=True)
    success_stories = {
        "SRCC": ["Economics Hons"],
        "LSR": ["English Hons", "BCom Hons", "Mathematics Hons"],
        "Hindu": ["Bcom Hons", "Mathematics Hons", "Statistics Hons"],
        "Hansraj": ["Bcom Hons", "BA Prog"],
        "KMC": ["Economics Hons", "Statistics Hons"],
        "Ramjas": ["BCom Hons", "Physics hons"],
        "Miranda House": ["Mathematics Hons", "BA Prog"],
        "DRC": ["BA Prog", "Zoology Hons"],
        "IPCW": ["BCom Hons", "BA Prog"],
        "KMV": ["CS hons"],
        "Others": ["SGGSCC", "SGTB Khalsa", "Gargi", "JMC", "ARSD and more..."]
    }

    st.markdown('<div class="flex-container">', unsafe_allow_html=True)
    for college, courses in success_stories.items():
        st.markdown(f"""
            <div class="card">
                <div class="card-title">{college}</div>
                <div class="card-content">{", ".join(courses)}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Floating Buttons
st.markdown("""
    <div class="floating-container">
    <a href="https://bit.ly/InsideDU_WACommunity" target="_blank" tooltip="Join our Community">
        <button class="floating-button">📱</button>
    </a>
    <a href="https://instagram.com/edu.insidedu" target="_blank">
        <button class="floating-button floating-button-instagram">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/900px-Instagram_icon.png?20200512141346" style="width:26px; height:26px;">    
        </button>
    </a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Inside DU Community © 2024</div>', unsafe_allow_html=True)