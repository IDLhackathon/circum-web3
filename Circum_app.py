import streamlit as st
import pandas as pd
from scripts import Foam, wallet
#General settings
st.set_page_config(
    page_title="Circum",
    page_icon="👋",
    layout="wide",
)


st.title("#Welcome on Circum App: WAZE of millitary applications")
st.header("create profile of user")
st.sidebar.markdown("")


with st.form(key='form_1'):
	long = st.text_input(label='Enter longitude')
	lat = st.text_input(label='Enter latitude')
	zoom = st.text_input(label='Enter a zoom value')

	submitted = st.form_submit_button(label='Submit')

if submitted:
    st.write(long + lat + zoom)