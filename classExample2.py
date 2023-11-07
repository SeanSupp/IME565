import streamlit as st
import pickle
import math
import pandas as pd

import sklearn
from sklearn.tree import DecisionTreeClassifier

# Package for data partitioning
from sklearn.model_selection import train_test_split

# Package to visualize Decision Tree
from sklearn import tree

# Package for generating confusion matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Package for generating classification report
from sklearn.metrics import classification_report

# Module to save and load Python objects to and from files
import pickle 


#============================================================
# Reading the pickle files that we created before 
dt_pickle = open('decision_tree_penguin.pickle', 'rb') 
map_pickle = open('output_penguin.pickle', 'rb') 
clf = pickle.load(dt_pickle) 
unique_penguin_mapping = pickle.load(map_pickle) 
dt_pickle.close() 
map_pickle.close() 

df_penguins = pd.read_csv('penguins.csv')

# Output column for prediction
output = df_penguins['species'] 

# Input features (excluding year column)
features = df_penguins[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']] 

# One-hot-encoding for categorical variables
features = pd.get_dummies(features)  #If the type of a variable is a string, then we don't need to explicitly insert

# Factorize output feature (convert from string to number)
output, uniques = pd.factorize(output)

#CV
train_X, test_X, train_y, test_y = train_test_split(features, output, test_size = 0.2, random_state = 1) 

clf = DecisionTreeClassifier(random_state = 0)

# Fitting model on training data
clf.fit(train_X, train_y) 

#Predicting the model
y_pred = clf.predict(test_X)

island = st.selectbox('Penguin Island', options = ['Biscoe', 'Dream', 'Torgerson']) 
sex = st.selectbox('Sex', options = ['Female', 'Male']) 

# For numerical variables, using number_input
# NOTE: Make sure that variable names are same as that of training dataset
bill_length_mm = st.number_input('Bill Length (mm)', min_value = 0) 
bill_depth_mm = st.number_input('Bill Depth (mm)', min_value = 0) 
flipper_length_mm = st.number_input('Flipper Length (mm)', min_value = 0) 
body_mass_g = st.number_input('Body Mass (g)', min_value = 0) 

# st.write('The user inputs are {}'.format([island, sex, bill_length, bill_depth, flipper_length, body_mass]))

# Putting sex and island variables into the correct format
# so that they can be used by the model for prediction
island_Biscoe, island_Dream, island_Torgerson = 0, 0, 0 
if island == 'Biscoe': 
  island_Biscoe = 1 
elif island == 'Dream': 
  island_Dream = 1 
elif island == 'Torgerson': 
  island_Torgerson = 1 

sex_female, sex_male = 0, 0 
if sex == 'Female': 
  sex_female = 1 
elif sex == 'Male': 
  sex_male = 1 

# Using predict() with new data provided by the user
new_prediction = clf.predict([[bill_length_mm, bill_depth_mm, flipper_length_mm, 
  body_mass_g, island_Biscoe, island_Dream, island_Torgerson, sex_female, sex_male]]) 

# Map prediction with penguin species
prediction_species = unique_penguin_mapping[new_prediction][0]

# Show the predicted species on the app
st.subheader("Predicting Your Penguin's Species")
st.write('We predict your penguin is of the {} species'.format(prediction_species)) 

#================================================================================================
#Users upload the CSV file(s) part

# Reading the pickle files that we created before 
dt_pickle = open('decision_tree_penguin.pickle', 'rb') 
map_pickle = open('output_penguin.pickle', 'rb') 
clf = pickle.load(dt_pickle) 
unique_penguin_mapping = pickle.load(map_pickle) 
dt_pickle.close() 
map_pickle.close() 

penguin_file = st.file_uploader ( " Select Your Local Penguins CSV (default provided ) " )

if penguin_file is not None :
    penguins_df = pd.read_csv(penguin_file) # User provided file
else:
    st.write("Please fill out the features") 
    


