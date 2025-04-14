import os
import numpy as np
from pathlib import Path
import streamlit as st
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model as tf_load_model

# ========== THEME CONFIGURATION ==========
def set_app_theme():
    st.markdown("""
    <style>
    :root {
        --primary: #FFD700;  /* Gold/Yellow */
        --secondary: #800000;  /* Maroon */
        --accent: #228B22;  /* Forest Green */
        --background: #FFF9E6;  /* Light Yellow */
        --text: #333333;
    }
    
    .stApp {
        background-color: var(--background);
        color: var(--text);
    }
    
    h1, h2, h3 {
        color: var(--secondary) !important;
    }
    
    .stButton>button {
        background-color: var(--secondary) !important;
        color: white !important;
        border: 2px solid var(--accent) !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
    }
    
    .stButton>button:hover {
        background-color: var(--accent) !important;
        border-color: var(--secondary) !important;
    }
    
    .stFileUploader>div>div {
        border: 2px dashed var(--secondary) !important;
        background-color: rgba(255, 215, 0, 0.1) !important;
    }
    
    .stExpander {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid var(--primary) !important;
        border-radius: 8px !important;
    }
    
    .stAlert {
        background-color: rgba(255, 215, 0, 0.2) !important;
        border-left: 4px solid var(--secondary) !important;
    }
    
    .diagnosis-card {
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        background: linear-gradient(145deg, #FFFFFF, #FFF9E6);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 5px solid var(--secondary);
    }
    
    .treatment-card {
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        background-color: rgba(34, 139, 34, 0.1);
        border-left: 5px solid var(--accent);
    }
    </style>
    """, unsafe_allow_html=True)

# ========== APP CONTENT ==========
def main():
    set_app_theme()
    
    st.title("🌻 Sunflower Health Guardian")
    st.markdown("""
    <div style="background-color: rgba(255, 215, 0, 0.2); padding: 15px; border-radius: 10px; 
                border-left: 5px solid #800000; margin-bottom: 20px;">
        Upload a sunflower leaf image to detect diseases and get treatment recommendations
    </div>
    """, unsafe_allow_html=True)
    
    # Model loading and prediction functions would go here
    # (Keep your existing model loading and prediction code)
    
    uploaded_file = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        col1, col2 = st.columns([1, 1.2])
        
        with col1:
            st.image(uploaded_file, use_container_width=True, 
                    caption="Your sunflower leaf", output_format="JPEG")
            
            if st.button("🔍 Diagnose", type="primary"):
                # Your prediction logic here
                diagnosis = "Graymold"  # Example - replace with actual prediction
                confidence = 0.92  # Example
                
                st.session_state.diagnosis = diagnosis
                st.session_state.confidence = confidence
        
        with col2:
            if 'diagnosis' in st.session_state:
                diagnosis = st.session_state.diagnosis
                confidence = st.session_state.confidence
                
                # Diagnosis Card
                st.markdown(f"""
                <div class="diagnosis-card">
                    <h2 style="color: #800000;">Diagnosis Result</h2>
                    <p><strong style="color: #228B22;">{diagnosis}</strong> with {confidence:.0%} confidence</p>
                    <div style="height: 10px; background: linear-gradient(90deg, #FFD700, #800000); 
                                border-radius: 5px; margin: 10px 0;"></div>
                </div>
                """, unsafe_allow_html=True)
                
                # Treatment Section
                st.markdown("""
                <div class="treatment-card">
                    <h3 style="color: #228B22;">💊 Recommended Treatment</h3>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("🛠️ Detailed Treatment Plan", expanded=True):
                    st.markdown("""
                    - **Immediate Action:** Remove affected leaves
                    - **Organic Treatment:** Apply neem oil solution
                    - **Chemical Control:** Fungicide every 7-10 days
                    - **Prevention:** Improve air circulation
                    """)
                
                # Prevention Tips
                st.markdown("""
                <div class="treatment-card">
                    <h3 style="color: #228B22;">🛡️ Prevention Tips</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                - Water at soil level (not leaves)
                - Space plants 24-36 inches apart
                - Apply balanced fertilizer monthly
                - Monitor plants weekly
                """)

if __name__ == "__main__":
    main()