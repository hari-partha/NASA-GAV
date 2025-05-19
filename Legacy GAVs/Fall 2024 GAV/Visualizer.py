import json
import math
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from gen_images import generate_image
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageOps import scale
from itertools import groupby
from statistics import mean
from streamlit_image_zoom import image_zoom


st.set_page_config(layout="wide")

col1, col2 = st.columns([5, 1])  # Adjust the ratio as needed
# with col2:
#     st.image('icon_folder/nbisc_logo.png', width=100)


def set_background_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0)), url({url});
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* Targeting the HTML elements directly for demonstration */
        h1, .title {
            color: #ffffff; /* White text color */
            text-shadow: 0 0 10px #00a1ff, 0 0 20px #00a1ff, 0 0 30px #00a1f7; /* Light Blue glow */
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )

with col1:
    
    set_background_image('https://t3.ftcdn.net/jpg/02/32/74/34/360_F_232743479_Zzil5APYDHoBrUk7qfH7eYyq5KW0nV0C.jpg')
    
    # Example of using inline styling for semi-transparent background on a specific text block
    apply_custom_styles()
    
    st.title("Welcome to NBISC Visualizer!")
    st.markdown("Please enter info to get started and generate your graphical abstract!")
    # ... Insert the rest of your content that should be inside the semi-transparent box here ...

    pi_name = st.sidebar.text_input('Name of Primary Investigator')
    pi_institution = st.sidebar.text_input('Location of Primary Investigator')

    experimental_title = st.sidebar.text_input('Experiment Title', key='experiment_title')
    
    experimental_location = st.sidebar.selectbox(
        'Where were the subjects irradiated?',
        options=['Brookhaven National Labs (NSRL)' , 'LBNL', 'Other'],
        index=0  
    )

    exp_type = st.sidebar.selectbox(
    "What type of experiment are you running",
    options = ['Radiation', 'Spaceflight'],
    index = 0)


    animal_type = st.sidebar.selectbox(
    'What species are your subjects?',
    options=['Mus Musculus', 'Sus Scofa', 'other'],
    index=0  
    )

    if animal_type == 'Mus Musculus':
        animal_strain = st.sidebar.text_input(
            'What is the mice strain?'
            )
        animal_strain = animal_strain.strip().upper() + ' ' + animal_type
    elif animal_type == 'other':
        animal_strain = st.sidebar.text_input(
            'What is the model organism strain and type (i.e. C57BL/6J Mice)?'
            )
        animal_strain = animal_strain.strip()
    else:
        animal_strain = 'Strain Unknown' + animal_type
        

    genotype = st.sidebar.text_input(
        "What is the genotype of the organism")

   
    bool_form = st.sidebar.selectbox(
    'Do you have an excel datasheet of the experiment?',
    options=[True, False],
    index=0  
    )
    if bool_form:
        uploaded_file = st.file_uploader("Upload Excel Sheet", type=['xlsx'])
        if uploaded_file is not None:
            df_dict = pd.read_excel(uploaded_file, sheet_name = None)
            print(df_dict.keys())
        img_list = []
        if st.button('Generate Image'):
                for sheet in df_dict.keys():
                    print(sheet)
                    df = df_dict[sheet]
                    group_data = df[1:]
                    group_data.columns = df.iloc[0]
                    # print(group_data)
                    pi_info = [str(experimental_title), str(pi_name), str(pi_institution), str(experimental_location)]
                    exp_info = [str(exp_type), str(animal_type), str(animal_strain), str(genotype)]
                    img = generate_image(pi_info, exp_info, group_data, sheet)
                    image_zoom(img, mode="dragmove", size=(1400, 750), keep_aspect_ratio=False, zoom_factor=2.0, increment=0.2)
       

            
