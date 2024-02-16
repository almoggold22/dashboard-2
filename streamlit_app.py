import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#Display Title and Despcriptio
st.title("Hello")
st.markdown("My Dashboard")

#Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

#Fetch existing vendors data
existing_data = conn.read(worksheet='Vendors', usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how='all')

st.dataframe(existing_data)