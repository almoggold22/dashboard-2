import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px

#Display Title and Despcription
st.title("Hello")
st.markdown("My Dashboard")

#Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

url = 'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit'

#Fetch existing vendors data
existing_data = conn.read(spreadsheet=url, worksheet='0', usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how='all')

st.dataframe(existing_data)
st.text_area("type something...")

chart = px.pie(existing_data,names='almog')
st.write(chart)
