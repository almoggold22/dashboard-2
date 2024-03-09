import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hello",
    layout='wide')

st.sidebar.success("Select a Page above")

#Compare Page:
#Display Title and Despcription
st.title(":grey[Feedbacks Dashboard] :green[All] - **Compare**")
st.markdown('**Data - Tool - All**')
st.markdown("")
st.markdown("")


#Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)
url = 'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit'

#---API Part Up To Here----------------------------------------------------------------------------------------------------------------------------------------

#-1-Set Connection with gsheets page:
left_chart = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)
right_chart = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)

#left - list of date's columns names and chosen buttons:
models_dates_col_left = ['Translation in', 'Intents', 'Embedding', 'AI21', 'Rephrase', 'Translation out', 'Entire flow', 'Score']
buttons_col_of_each_model_left = ['Translation in buttons1', 'Intents buttons1', 'Closest questions (embedding) buttons1', 'Contextual answer (AI21) buttons1', 'Rephrase buttons1', 'Translation out buttons1', 'Entire flow buttons1', 'Score buttons1']

#create right and left columns on streamlit for choosing model:
col_model_left, col_model_middle, col_model_right = st.columns((3))
with col_model_middle:
    model_type_left = st.selectbox("Choose Model (Left)", models_dates_col_left)


#Dates Range
if model_type_left:
    left_chart[model_type_left] = pd.to_datetime(left_chart[model_type_left])
    today1 = conn.read(spreadsheet=url, worksheet='1710462852', usecols=list(range(1)), ttl=5)
    start_date_1 = pd.to_datetime(left_chart[model_type_left]).min()
    end_date_1 = pd.to_datetime(today1['today']).max()
    start_date_2 = pd.to_datetime(right_chart[model_type_left]).min()
    end_date_2 = pd.to_datetime(today1['today']).max()

col1, col2, middle, col4, col5 = st.columns((5))
#---Make dates as columns---
with col1:
    date1 = pd.to_datetime(st.date_input("Start date", start_date_1, key=1))

with col2:
    date2 = pd.to_datetime(st.date_input("End date", end_date_1, key=2))

with col4:
    date3 = pd.to_datetime(st.date_input("Start date", start_date_2, key=3))

with col5:
    date4 = pd.to_datetime(st.date_input("End date", end_date_2, key=4))

#set range and terms for columns (gt, lt, eq)
left_range = left_chart[(left_chart[model_type_left] >= date1) & (left_chart[model_type_left] <= date2)].copy()
right_range = left_chart[(left_chart[model_type_left] >= date3) & (left_chart[model_type_left] <= date4)].copy()
#------------------- Up to here Date Part

#functions to fine the index of the relevant buttons' column and use it on pie charts:
def index_finder_left(models_dates_col_left):
    for model in models_dates_col_left:
        if model_type_left == model:
            name_of_buttons_col_left = models_dates_col_left.index(model_type_left)
            return name_of_buttons_col_left

#columns for pie charts
col_model1, col_model2, col_model3, col_model4, col_model5 = st.columns((5))
#---2---Pie-Charts--
#'translation in' columns - left side
existing_data_left = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)
size_left = left_range.groupby(buttons_col_of_each_model_left[index_finder_left(models_dates_col_left)]).size()
pie_chart_left = px.pie(left_range, values=size_left, names=size_left.index, height = 500, width= 450, hole=.4)
df_left_all = pd.DataFrame(size_left)


#'intents' columns - right side
existing_data_right = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)
size_right = right_range.groupby(buttons_col_of_each_model_left[index_finder_left(models_dates_col_left)]).size()
pie_chart_right = px.pie(right_range, values=size_right, names=size_right.index, height = 500, width= 450, hole=.4)
df_right_all = pd.DataFrame(size_right)

with col_model1:
    st.plotly_chart(pie_chart_left)
with col_model4:
    st.plotly_chart(pie_chart_right)

dfcolall1, dfcolall2, dfcolall3, dfcolall4, dfcolall5 = st.columns((5))
with dfcolall1:
    dfcol_left = st.dataframe(df_left_all, width=340)
with dfcolall4:
    dfcol_right = st.dataframe(df_right_all, width=340)

st.divider()
