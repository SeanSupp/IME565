import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

dt_pickle = open('decision_tree_reg_bike.pickle', 'rb') 
regDSTree = pickle.load(dt_pickle) 
dt_pickle.close() 

bike_file = st.file_uploader('Upload your own bike data to train the model') 

df_bike7 = pd.read_csv('bike_lab7.csv')
df_bike_user = pd.read_csv('bike_user.csv')



with st.form('user_inputs'): 
  season = st.selectbox('Seasons', options=df_bike7['season'].unique()) 
  mnth = st.selectbox('Month', options=df_bike7['mnth'].unique()) 
  holiday = st.selectbox('Holiday', options=df_bike7['holiday'].unique())
  weekday = st.selectbox('Weekday', options=df_bike7['weekday'].unique())
  workingday = st.selectbox('workingday', options=df_bike7['workingday'].unique())
  weathersit = st.selectbox('weathersit', options=df_bike7['weathersit'].unique())
  temp = st.number_input('Temperature') 
  atemp = st.number_input('atemp') 
  hum = st.number_input('Hum')
  windspeed = st.number_input('windspeed') 
  st.form_submit_button()


if bike_file is None:
  
  df_bike7 = pd.read_csv('bike_lab7.csv')
  df_bike7 = df_bike7.drop(columns=['cnt'])
  row_user_input = [season, mnth, holiday, weekday, workingday,weathersit, temp, atemp, hum, windspeed]
  df_bike7.loc[len(df_bike7)] = row_user_input

  df_bike7.dropna()
 

  combined_df_encoded = pd.get_dummies(df_bike7)
  user_row = combined_df_encoded.tail(1)

 

  pred_user = regDSTree.predict(user_row)
  st.write('Predicted CNT')
  st.write(int(pred_user))
else:
  
  df_bike7 = pd.read_csv('bike_lab7.csv')
  df_bike_user = pd.read_csv(bike_file)

  df_bike7.dropna()
  df_bike_user.dropna()

  df_bike7 = df_bike7.drop(columns=['cnt'])

  combined_df_2 = pd.concat([df_bike7,df_bike_user],axis=0)

  orginal_rows_2 = df_bike7.shape[0]

  combined_df_encoded_2 = pd.get_dummies(combined_df_2)

  original_df_encoded_2 = combined_df_encoded_2[:orginal_rows_2]
  user_df_encoded_2 = combined_df_encoded_2[orginal_rows_2:]

  pred_user_2 = regDSTree.predict(user_df_encoded_2)

  df_bike_user['predicted_cnt'] = pred_user_2
  df_bike_user['predicted_cnt'] = df_bike_user['predicted_cnt'].round()

  st.write(df_bike_user)


st.subheader("Prediction Performance")
tab1, tab2 = st.tabs(["Decision Tree", "Feature Importance"])

with tab1:
  st.image('regDT.png')
with tab2:
  st.image('feature_imp_asgn7.png')






  










