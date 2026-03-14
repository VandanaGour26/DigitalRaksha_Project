
import streamlit as st
import base64
import deepfake
import phishing  


st.set_page_config(
    page_title="DigitalRaksha", 
    page_icon="🛡️", 
    layout="wide"
)

st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg, #E0EAFC, #CFDEF3);
        color: #1E293B;
        font-family: 'Poppins', sans-serif;
    }


    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 42px;
        font-weight: 800;
        margin-top: 10px;
        text-shadow: 1px 1px 2px #94A3B8;
        animation: fadeInDown 1s ease-in-out;
    }

    @keyframes fadeInDown {
        from {opacity: 0; transform: translateY(-30px);}
        to {opacity: 1; transform: translateY(0);}
    }


    .sub-title {
        text-align: center;
        color: #475569;
        font-size: 18px;
        margin-bottom: 30px;
    }


    .card {
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        padding: 25px;
        margin-top: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }

    div.stButton > button {
        background: linear-gradient(90deg, #3B82F6, #6366F1);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 25px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #2563EB, #4F46E5);
        transform: scale(1.05);
    }


    [data-testid="stSidebar"] {
        background-color: #F8FAFC;
        padding-top: 20px;
        box-shadow: 2px 0px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)


menu = ["Home 🏠", "Phishing Link Detector 🔗", "Deepfake Video Detector 🎭", "About 📘", "Team 👩‍💻"]
choice = st.sidebar.selectbox("📂 Menu", menu)

if choice == "Home 🏠":
    # Function to convert image to base64
    def get_base64_image(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Load logo image
    image_base64 = get_base64_image("deepfake.jpg")

    # Display centered logo
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 20px; margin-bottom: 10px;">
            <img src="data:image/png;base64,{image_base64}" width="180">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Title + Description
    st.markdown("""
    <h1 class='main-title' style="margin-left: 40px;">
    Welcome to DigitalRaksha 🛡️
    </h1>
      """, unsafe_allow_html=True)

    st.markdown("<p class='sub-title'>Protecting users from fake content & phishing links using AI</p>", unsafe_allow_html=True)

    # About Project
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 About the Project")
    st.write("""
    The **AI-Based Fake Content Detection System** is designed to detect:
    - 🔗 *Phishing Links* that can steal personal data  
    - 🎭 *Deepfake Videos* that manipulate human emotions  

    This project ensures **digital safety** and **trustworthy online interactions**.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Buttons
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("🔗 Try Link Detector")
    with col2:
        st.button("🎭 Try Video Detector")

elif choice == "Phishing Link Detector 🔗":
    phishing.app()

elif choice == "Deepfake Video Detector 🎭":
    deepfake.app()

elif choice == "About 📘":
    st.markdown("<h2 class='main-title'>About DigitalRaksha</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    **DigitalRaksha** is an AI-powered system developed to detect phishing links and deepfake videos.  
    It aims to make digital spaces more **secure**, **reliable**, and **user-friendly** using advanced AI models.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "Team 👩‍💻":
    st.markdown("<h2 class='main-title'>Meet the Team 👩‍💻</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    - 👩‍💻 **Mansi Sharma**  
    - 👩‍💻 **Mishika Sanotiya**  
    - 👩‍💻 **Nupur Rana**  
    - 👩‍💻 **Vandana Gour**
    """)
    st.markdown("</div>", unsafe_allow_html=True)
