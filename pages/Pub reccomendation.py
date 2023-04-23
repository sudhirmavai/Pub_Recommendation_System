import streamlit as st
import pandas as pd
import folium
import numpy as np
from folium.plugins import MarkerCluster
from folium import Marker
from streamlit_folium import folium_static

# setting page configuration
st.set_page_config(
    page_title="Pub Reccomendation",
    page_icon="👋",
)

# Reading data into pandas
pub = pd.read_csv('Cleaned and Processed pub data.csv')
pub.drop(['Unnamed: 0'], axis = 1 , inplace = True)

st.write("# Welcome to Pub Reccomendation System ! 👋")

st.sidebar.success("Fiter Pubs .")

st.header('Nerast pub based on your location')


# Allow user to enter their latitude and longitude
Latitude_ = st.number_input("Enter your latitude:", value=51.73)
Longtitude_ = st.number_input("Enter your longitude:", value=-4.72)

pub['Distance'] = np.sqrt((pub['Latitude'] - Latitude_)**2 + (pub['Longitude'] - Longtitude_)**2)

Nerast_5_pub = pub.sort_values(by = 'Distance').head()

st.dataframe(Nerast_5_pub)

Nerast_pub_map = folium.Map(location = [Nerast_5_pub['Latitude'].iloc[0] , Nerast_5_pub['Longitude'].iloc[0]] ,
                         zoom_start = 15 , tiles='openstreetmap')
for i in range(len(Nerast_5_pub)):
    folium.Marker([Nerast_5_pub['Latitude'].iloc[i] , Nerast_5_pub['Longitude'].iloc[i]] ,
                              popup=Nerast_5_pub['Name'].iloc[i], 
                tooltip=f'{i} Nerast Pub!',  icon=folium.Icon(color="blue", icon="cloud")).add_to(Nerast_pub_map)
            # Display the map
folium_static(Nerast_pub_map)
