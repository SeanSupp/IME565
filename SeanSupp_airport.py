import streamlit as st
import pickle
import math
import pandas as pd

st.title("Haversine Distance Calculator")
st.write("Latitude takes input as 0° at the equator to 90°N (90) or 90°S (-90)at the poles -- ranges from -90 to 90 " 
         "Longtitude takes input 0° at the prime meridian to 180°E (180) or 180°W (-180) -- ranges from -180 to 180"
        )
a = st.number_input('Enter latitute of the first location', min_value=-90.00)
b = st.number_input('Enter Longtitude of the first location', min_value=-180.00)
c = st.number_input('Enter latitute of the second location', min_value=-90.00)
d = st.number_input('Enter Longtitude of the second location', min_value=-180.00)

def haversineDistance(a,b,c,d):
#converting from deg to rad
    lat_a = math.radians(a)
    long_a = math.radians(b)
    lat_b = math.radians(c)
    long_b = math.radians(d)

    #formula for "a" distance
    haversine_a = ((math.sin((lat_b-lat_a)/2))**2) + (math.cos(lat_a)*math.cos(lat_b)*((math.sin((long_b-long_a)/2))**2))

#formula for "c" distance
    haversine_c = 2 * math.atan2(math.sqrt(haversine_a),math.sqrt(1-haversine_a))

#formula for "d" distance
    haversine_d = int(6371 * haversine_c)
    return int(haversine_d)

#outputing the Haversine distance
st.write(f'Your distance is: {haversineDistance(a,b,c,d)} km') 

st.title("Fine Nearest Airports")

airportCode = st.selectbox('Select Airport Code', options = ['CDG', 'CHC', 'DYR', 'EWR', 'HNL', 'OME', 'ONU', 'PEK']) 

df_airport = pd.read_csv('airport_location.csv')

def findNearestAirports(airport_code):
    if airport_code not in df_airport['Airport Code'].values:
        return "Airport code not found in the DataFrame."

    # Filter the DataFrame to exclude the given airport
    df_filtered = df_airport[df_airport['Airport Code'] != airport_code]

    # Calculate Haversine distances and add a new 'Distance' column
    df_filtered['Distance'] = df_filtered.apply(
        lambda x: haversineDistance(
            df_airport[df_airport['Airport Code'] == airport_code]['Lat'].values[0], #select lat for the given airport code
            df_airport[df_airport['Airport Code'] == airport_code]['Long'].values[0], #select long for the given airport code
            x['Lat'],
            x['Long']
        ),
        axis=1
    )

    # Sort the DataFrame by distance and select the top num_airports
    nearest_airports = df_filtered.sort_values(by='Distance').reset_index().drop('index',axis=1)

    return nearest_airports


st.write(findNearestAirports(airportCode))

