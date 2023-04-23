import streamlit as st

# setting page configuration
st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to Pub Reccomendation System ! 👋")

st.sidebar.success("Description of project.")

st.markdown(
    """
    This is pub reccomendation system for United kingdom.
    This website will halp you to find pubs in UK by
    Local Area , Postal Code ,
    You can also search nearest pub by your location
   **👈 Select another page from the sidebar**
    ### About us?
    - Check out [Linkedin Profile](https://www.linkedin.com/in/sudhir-data-science/)
    - Check out [Kaggle Profile](https://www.kaggle.com/sudhirsingh108)
    - See our more interesting project [Github Profile](https://github.com/sudhirmavai)
    """

)
st.image('image.jpg' , use_column_width=True)

st.markdown ( """
      ### Did You Know
    -  The city with the most pubs per square mile, 
       Portsmouth has almost double the number of pubs per square mile than London.
    -  The Red Lion is the most common pub name in the UK
    -  There are around 50,000 pubs in the UK  
"""
)