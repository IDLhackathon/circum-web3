import streamlit as st
import sys
import importlib.util
import os
from scripts import wallet
#General settings
st.set_page_config(
    page_title="ocean-marketplace",
    page_icon="👋",  
)



#import wallet
st.title("Create data certificate @ OCEAN_Protocol")

# Create a form
with st.form(key="form"):
    st.header("image details ")

    # Upload image button and display uploaded image
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    
    name = st.text_area("name", help="adding the name of the publisher") 
    # email 
    email = st.text_area("email", help="writing your personal email")
    
    # Description input
    description = st.text_area("Description", help="Write a brief description")

    # Tags input (multi-select)
    tags_options = ["Millitary vehicles", "trench-warfare", "civilian building", "regroupment"]
    tags = st.multiselect("Tags", tags_options, help="Select one or more tags")

    # Terms & Conditions tickmark
    terms_and_conditions = st.checkbox("I accept T&C", value=False)
    # dataset_type

    asset_type_options = ["Image", "Cartograph"]
    selected_asset_types = st.selectbox("Asset Type", asset_type_options)

    # Submit button
    submit_button = st.form_submit_button("Submit")

col1, col2, _ = st.columns([1, 1, 3])

with col1:
    with st.expander("Account infromation", expanded=True):
        st.write("account information: 0x.....")
        st.write("account dataTokens: 10 DT")
    # Add more content to the card if needed

# Process the form data after submission
if submit_button:
    if terms_and_conditions:
        
        
        #wallet_created =  Wallet(name=name, email=email)
        wallet = wallet()
        st.success("Form submitted successfully")
        st.write("wallet created")
        st.write("Description:", description)
        st.write("Tags:", tags)

    else:
        st.error("Please accept the terms and conditions to submit the form")
