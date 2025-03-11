import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
import time
import datetime
st.title(' App Ubicacion')

st.write('Ubicación')

# Display the current date and time
current_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
st.write(f"Current time: {current_time}")
loc = get_geolocation() 



# Extract latitude and longitude
latitude = loc['coords']['latitude']
longitude = loc['coords']['longitude']

# Button to fetch location details
if st.button("Get Location"):
    st.write(f"Current time: {current_time}")
    # Create a Google Maps link
    st.write(f"[Google Maps](https://www.google.com/maps/search/?api=1&query={latitude},{longitude})")

