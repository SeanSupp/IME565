# Import packages
import streamlit as st
import pandas as pd
import matplotlib . pyplot as plt
import seaborn as sns
# Main title of the app
st.title ( " Palmer ’s Penguins " )

# Our subtitl
st.markdown( " Use this Streamlit app to make your own scatterplot about penguins ! " )

penguin_file = st.file_uploader ( " Select Your Local Penguins CSV (default provided ) " )

if penguin_file is not None :
    penguins_df = pd.read_csv(penguin_file) # User provided file
else:
    penguins_df = pd.read_csv ( "penguins.csv" ) # Default file


selected_x_var = st.selectbox("What do you want the x variable to be ?" ,["bill_length_mm" , "bill_depth_mm" , "flipp er_len gth_mm" , "body_mass_g" ] ,)

selected_y_var = st.selectbox("What about the y ?" ,[ "bill_depth_mm" , "bill_length_mm" , "flipp er_len gth_mm" , "body_mass_g" ] ,)

sns.set_style( "darkgrid")

markers = {"Adelie": "X" , "Gentoo" : "s" , "Chinstrap" : "o" }

palette = { "Adelie" : "green" , "Gentoo" : "blue" , "Chinstrap" : "orange" }

