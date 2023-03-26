import streamlit as st
import pandas as pd
from scripts import Foam, wallet
from dotenv import dotenv_values

#General settings
config = dotenv_values(".env")
count = 0
st.set_page_config(
    page_title="Circum",
    page_icon="👋",
    layout="wide",
)


st.title("#Welcome on Circum App")
st.text("1. create user profile")
st.text("2. go to the market application in order to publish yolo image")
st.sidebar.markdown("")


with st.form(key='Registeration'):
	longitude = st.text_input(label='enter alias name')
	lat = st.text_input(label='place')
	zoom = st.text_input(label='profession(publisher)')

	submitted = st.form_submit_button(label='Submit')

if submitted:
    st.write("creating the user profile at address")
    userw = wallet.Wallet(longitude, lat)
    st.write(userw.get_address())
    st.write("creating the user profile")
    # foamContract = Foam.Foam()
    # informat_contact = lat + longitude + zoom
    # hexDetails = hex(int(informat_contact,16))
    # inputBytes = bytes.fromhex(hexDetails)
    st.write("now validating the coordinates by the admin")
    # THE FOLLOWING NEEDS TO NOT HAVE PRIV KEY (its done for quick demo purposes
    #  AND SHOULD NOT BE DEPLOYED ON PROD.
    # foamContract.init_user_information(count,userw.get_address(),inputBytes, userw.get_address(),config["PRIVATE_KEY"])
    st.write("now admin validating the user score (out of 100): 50 ")
    st.write("registeration successful")
    # foamContract.set_user_score(1,100,userw.get_address(),config["PRIVATE_KEY"])

