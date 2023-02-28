import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import image

st.set_page_config(page_title="My First App",page_icon=":smiley:", layout="wide",)


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "app.jpg")

st.title("MyFirst App:tada:")
st.write("Hello There")
st.write("I am Nikitha")

if st.button('About Me'):
    st.write("Data Science Intern at Innomatics Research Labs")
    st.write("I have completed my MBA and currently pursuing Data Science")
    st.write("Email_Id : nikithaniki1413@gmail.com")
    st.write("Linkedin : https://www.linkedin.com/in/nikitha-b-84042b212/")
    st.write("github:https://github.com/niki1413/data_science_internship23")