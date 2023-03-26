import streamlit as st
import pandas as pd
import importlib.util
#import sys
#sys.path.append('.')
import model_yolo
from PIL import Image

#General settings
st.set_page_config(
    page_title="Cassini",
    page_icon="👋",
    layout="wide",
)

st.markdown("<h1 style='text-align: center; color: black;text-shadow: 2px 4px 3px rgba(0,0,0,0.3);margin-top: 0px;'>Enabling cross-terrain mobility</h1>", unsafe_allow_html=True)

st.text("")
st.text("")

st.markdown("<h1 style='color: black;text-decoration:underline solid #000000;font-size:25px'>Choose geographical coordinate</h1>", unsafe_allow_html=True)

st.sidebar.markdown("# Welcome on Circum App !")

with st.form(key='form_1'):
    uploaded_file = st.file_uploader("Choose an image")
    submitted = st.form_submit_button(label='Submit')
    
if submitted:
    img = model_yolo.predict_img() 
    st.image(img, caption='Object detection')
    