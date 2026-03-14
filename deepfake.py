import streamlit as st

def app():
   
    st.set_page_config(page_title="Truth Scanner | Deepfake Detection", page_icon="🎥", layout="centered")

 
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #E0EAFC 0%, #CFDEF3 100%);
            font-family: 'Poppins', sans-serif;
        }


        .main-title {
            text-align: center;
            color: #0f172a;
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            color: #1e3a8a;
            font-size: 18px;
            margin-bottom: 25px;
        }

 
        .upload-section {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
        }


        div.stButton > button {
            background: linear-gradient(to right, #00BFFF, #009ACD);
            color: white;
            border-radius: 8px;
            height: 45px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(to right, #38bdf8, #0284c7);
        }


        .features-section {
            margin-top: 50px;
            padding: 40px 25px;
            text-align: center;
        }
        .features-section h2 {
            color: #0f172a;
            font-size: 34px;
            font-weight: 700;
            margin-bottom: 25px;
        }

        .feature-box {
            background: linear-gradient(145deg, #ffffff, #e0f7ff);
            border: 1px solid #b3e5fc;
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-box:hover {
            transform: translateY(-6px);
            box-shadow: 0 8px 25px rgba(33, 150, 243, 0.3);
        }

        .feature-title {
            font-size: 22px;
            color: #0284c7;
            font-weight: 600;
            margin-bottom: 10px;
       
        }

        .feature-desc {
            font-size: 16px;
            color: #334155;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 15px;
            color: #1e293b;
        }
        </style>
    """, unsafe_allow_html=True)


    st.markdown("<h1 class='main-title'>🎥 Truth Scanner</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>AI-Powered Deepfake Detection for Safer Digital Media</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
    st.subheader("📤 Upload Your Video for Analysis")
    video = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mkv"])

    if st.button("🚀 Upload & Analyze"):
        if video is not None:
            st.info("🔍 Processing your video... Please wait.")
            # Placeholder for model output
            st.success("✅ Analysis Complete! The video appears authentic.")
        else:
            st.warning("⚠️ Please upload a video first.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='features-section'>", unsafe_allow_html=True)
    st.markdown("<h2>✨ Key Features</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-title' >🤖 AI-Powered Detection</div>
            <div class='feature-desc'>Detects deepfake videos using cutting-edge deep learning models for highly accurate results.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-title'>⚡ Real-Time Analysis</div>
            <div class='feature-desc'>Processes your videos quickly and provides immediate authenticity reports.</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-title'>📊 Confidence Scoring</div>
            <div class='feature-desc'>Displays a probability score showing how confident the AI is about the result.</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


    st.markdown("<p class='footer'>🔐 Stay Safe — Verify Before You Trust!</p>", unsafe_allow_html=True)
