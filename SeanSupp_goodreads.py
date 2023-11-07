import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')


df_goodreads = pd.read_csv('goodreads_history.csv')

#How many books does the user read each year?
df_goodreads['Date Added'] = pd.to_datetime(df_goodreads['Date Added'], format = '%Y/%m/%d')
df_goodreads['year'] = df_goodreads['Date Added'].dt.year


plt.bar(df_goodreads['year'], df_goodreads['Read Count'])
plt.xticks(df_goodreads['year'].unique())
plt.xlabel("Year")
plt.ylabel("Number of books the user read")
plt.title("How many books does the user read each year?");

#How long does it take for the user to finish a book that they have started?
df_goodreads['Date Added'] = pd.to_datetime(df_goodreads['Date Added'], format = '%Y/%m/%d')
df_goodreads['Date Read'] = pd.to_datetime(df_goodreads['Date Read'], format = '%Y/%m/%d')
df_goodreads['date_diff'] = df_goodreads['Date Read'] - df_goodreads['Date Added']
df_goodreads['days_diff']= df_goodreads['date_diff'].dt.days
days_nonzero = df_goodreads[df_goodreads['days_diff'] >= 0.0]
plt.hist(days_nonzero['days_diff'], bins=10,color='salmon',edgecolor='black')
plt.xlabel("Days")
plt.title("How long does it take for the user to finish a book that they have started?");

#How long are the books that they have read?
plt.hist(df_goodreads['Number of Pages'], bins=10,color='green',edgecolor='black')
plt.xlabel("Number of pages")
plt.title("How long are the books that they have read?");


#How old are the books that they have read?
year_counts = df_goodreads['Year Published'].value_counts().sort_index()
year_counts.plot(kind='bar')
plt.xlabel('Year Published')
plt.ylabel('Count')
plt.title('How old are the books that they have read?')

#How do the user rate books compared to other Goodreads users? Two samples t-test?
plt.hist(df_goodreads['My Rating'], bins=3, edgecolor='k')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of users ratings')

plt.hist(df_goodreads['Average Rating'], bins=3, edgecolor='k')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of others ratings')

st.subheader("Visualization summary of series of questions related to goodreads.csv")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["How many books does the user read each year?",
                                               "How long does it take for the user to finish a book that they have started?",
                                               "How long are the books that they have read?",
                                               "How old are the books that they have read?",
                                               "How do the user rate books compared to other Goodreads users?"])

with tab1:
  st.image('How many books does the user read each year?.png')
with tab2:
  st.image('How long does it take for the user to finish a book that they have started?.png')
with tab3:
  st.image('How long are the books that they have read?.png')
with tab4:
  st.image('How old are the books that they have read?.png')
with tab5:
  st.image("Distribution of users ratings.png")
  st.image('Distribution of others ratings.png')
  st.write('On average, the user tends to give lower ratings compared to other users')

