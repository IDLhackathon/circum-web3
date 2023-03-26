import streamlit as st
import sys
import importlib.util
import os
from scripts import wallet
from scripts.Foam import Foam
from dotenv import dotenv_values
import time
import random, string

#General settings
st.set_page_config(
    page_title="ocean-marketplace",
    page_icon="👋",  
)


st.title("Create data certificate for obstacle detection")

## TODO: integrate the infura endpoint to transfer the details


def generate_mock_hash():
    # generate a random transaction hash
    transaction_hash = ''.join(random.choices(string.ascii_lowercase + string.digits, k=64))

    # construct the Etherscan URL for the transaction hash
    etherscan_url = f"https://mumbai.polygonscan.com/address/0xeb1C79E2632acf0c699C27c58e4e7D4557A60cF7#readContract"

    # display the transaction hash as a link to Etherscan
    return f"[{transaction_hash}]({etherscan_url})"



# Create a form
with st.form(key="form"):
    st.header("image details ")

    # Upload image button and display uploaded image
    uploaded_file = st.file_uploader("Upload the image regarding", type=["png", "jpg", "jpeg"])
    
         
    if uploaded_file: 
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        # with st.spinner("Running the upload..."):
        #     time.sleep(5)
        #     submit_image_analysis = st.form_submit_button("Submit for mock yolo verification")
     # display the result
        st.write("Result(%): 90 , category: cesna-airplane")
    
    name = st.text_area("name", help="adding the name of the publisher") 
    # email 
    email = st.text_area("email", help="writing your personal email")
    
    # Description input
    description = st.text_area("Description", help="Write a brief description")

    # Tags input (multi-select)
    tags_options = ["Millitary vehicles", "trench-warfare", "civilian building", "regroupment"]
    tags = st.multiselect("Tags", tags_options, help="Select one or more tags")

    terms_and_conditions = st.checkbox("I accept T&C", value=False)

    asset_type_options = ["Image", "Cartograph"]
    selected_asset_types = st.selectbox("Asset Type", asset_type_options)

    submit_button = st.form_submit_button("Submit")

    col1, col2, _ = st.columns([1, 1, 3])

    with col1:
        user_w = wallet.Wallet("test", "test@demo.com" )
        with st.expander("Account infromation", expanded=True):
            st.write("account information:",user_w.get_address())
            st.write("account dataTokens: 10 DT")
   
    if submit_button:
        if terms_and_conditions:
        
            st.success("Form submitted successfully")
            
            st.write("transaction hash Description:")
           
            st.markdown(generate_mock_hash(), unsafe_allow_html=True)

            st.write("Tags:", tags[0])

        else:
            st.error("Please accept the terms and conditions to submit the form")
