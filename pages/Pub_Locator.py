import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# setting page configuration
st.set_page_config(
    page_title="Pub Locator",
    page_icon="👋",
)

# Reading data into pandas
pub = pd.read_csv('Cleaned and Processed pub data.csv')
pub.drop(['Unnamed: 0'], axis = 1 , inplace = True)

st.write("# Welcome to Pub Reccomendation System ! 👋")

st.sidebar.success("Fiter Pubs .")

# Select between postal code or local authority to search pubs
filter_type = st.radio("Filter by:", ('Postal Code', 'Local Authority'))

if filter_type == 'Postal Code':
    Postal_code = st.text_input("Enter Postal Code", "Type Here ...")
    button_1 =  st.button('Click to search pub')
    if button_1:
        #Postal_code_enetred = Postal_code.title()
        uk_postal_code = pub['Postcode'].unique()
        if Postal_code in uk_postal_code:    
            data_by_postal = pub[pub['Postcode'] == Postal_code]
            st.dataframe(data_by_postal)

            Post_wise_map = folium.Map(location = [data_by_postal['Latitude'].iloc[0] , data_by_postal['Longitude'].iloc[0]] ,
                         zoom_start = 15 , tiles='openstreetmap')
    
            for i in range(len(data_by_postal)):
                folium.Marker([data_by_postal['Latitude'].iloc[i] , data_by_postal['Longitude'].iloc[i]] ,
                              popup=data_by_postal['Name'].iloc[i], 
                tooltip=f'{i} Pub!',  icon=folium.Icon(color="red", icon="cloud")).add_to(Post_wise_map)
            # Display the map
            folium_static(Post_wise_map)    

        else:
            st.error("Given post code does't exits in UK")    
else:
    Local_Authority = st.text_input("Enter the name Local Authority", "Type Here ...")
    button_1 =  st.button('Click to search pub')
    if button_1:
        Local_Authority_enetred = Local_Authority.title()

        all_loc_athority = pub['Loc_athurity'].unique()
        if Local_Authority_enetred in all_loc_athority:    
            data_by_athurity = pub[pub['Loc_athurity'] == Local_Authority_enetred]
            st.dataframe(data_by_athurity)

            Authority_wise_map = folium.Map(location = [data_by_athurity['Latitude'].iloc[0] , data_by_athurity['Longitude'].iloc[0]] ,
                         zoom_start = 15 , tiles='openstreetmap')
    
            for i in range(len(data_by_athurity)):
                folium.Marker([data_by_athurity['Latitude'].iloc[i] , data_by_athurity['Longitude'].iloc[i]] ,
                              popup=data_by_athurity['Name'].iloc[i], tooltip=f'{i} Pub!',  icon=folium.Icon(color="green",
                                                                         icon="info")).add_to(Authority_wise_map)
            # Display the map
            folium_static(Authority_wise_map)
        else:
            st.error("Given authority name does't exits in UK")

