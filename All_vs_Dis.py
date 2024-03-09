import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px


st.sidebar.success("Select a Page above")

#Compare Page:
#Display Title and Despcription
st.title(":grey[Feedbacks Dashboard] :green[All]")
st.markdown("**Compare**")

title_dis, title_all = st.columns((2))
with title_dis:
    st.markdown(":blue[**Dislike**]")
with title_all:
    st.markdown(":blue[**All**]")

#Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)
url = 'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit'

#---API Part Up To Here----------------------------------------------------------------------------------------------------------------------------------------

#-1-Set Connection with gsheets page:
left_chart_dis = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(9, 75)), ttl=5)
right_chart_all = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)

#left - list of date's columns names and chosen buttons:
models_dates_col_left_dis = ['Translation in', 'Intents', 'Embedding', 'AI21', 'Rephrase', 'Translation out', 'Entire flow', 'Score date']
buttons_col_of_each_model_left_dis = ['Translation in buttons1', 'Intents buttons1', 'Closest questions (embedding) buttons1', 'Contextual answer (AI21) buttons1', 'Rephrase buttons1', 'Translation out buttons1', 'Entire flow buttons1', 'Score buttons1']

#right - list of date's columns names and chosen buttons:
models_dates_col_right_all = ['Translation in', 'Intents', 'Embedding', 'AI21', 'Rephrase', 'Translation out', 'Entire flow', 'Score']
buttons_col_of_each_model_right_all = ['Translation in buttons1', 'Intents buttons1', 'Closest questions (embedding) buttons1', 'Contextual answer (AI21) buttons1', 'Rephrase buttons1', 'Translation out buttons1', 'Entire flow buttons1', 'Score buttons1']

#create right and left columns on streamlit for choosing model:
col_model_left_dis, col_model_right = st.columns((2))
with col_model_left_dis:
    model_type_left_dis = st.selectbox("Choose Model (Left)", models_dates_col_left_dis)

with col_model_right:
    model_type_right_all = st.selectbox("Choose Model (Right)", models_dates_col_right_all)

#Dates Range
if model_type_left_dis:
    left_chart_dis[model_type_left_dis] = pd.to_datetime(left_chart_dis[model_type_left_dis])
    today1 = conn.read(spreadsheet=url, worksheet='1710462852', usecols=list(range(1)), ttl=5)
    start_date_1_dis = pd.to_datetime(left_chart_dis[model_type_left_dis]).min()
    end_date_1_dis = pd.to_datetime(today1['today']).max()
    #----
if col_model_right:
    right_chart_all[model_type_right_all] = pd.to_datetime(right_chart_all[model_type_right_all])
    today2 = conn.read(spreadsheet=url, worksheet='1710462852', usecols=list(range(1)), ttl=5)
    start_date_2_all = pd.to_datetime(right_chart_all[model_type_right_all]).min()
    end_date_2_all = pd.to_datetime(today2['today']).max()

col1, col2, col3, col4 = st.columns((4))
#---Make dates as columns---
with col1:
    date1 = pd.to_datetime(st.date_input("Start date", start_date_1_dis))

with col2:
    date2 = pd.to_datetime(st.date_input("End date", end_date_1_dis))

with col3:
    date3 = pd.to_datetime(st.date_input("Intents Start date", start_date_2_all))

with col4:
    date4 = pd.to_datetime(st.date_input("Intents End date", end_date_2_all))

#set range and terms for columns (gt, lt, eq)
left_range_dis = left_chart_dis[(left_chart_dis[model_type_left_dis] >= date1) & (left_chart_dis[model_type_left_dis] <= date2)].copy()
right_range_all = right_chart_all[(right_chart_all[model_type_right_all] >= date3) & (right_chart_all[model_type_right_all] <= date4)].copy()
#------------------- Up to here Date Part

#functions to fine the index of the relevant buttons' column and use it on pie charts:
def index_finder_left_dis(models_dates_col_left_dis):
    for model in models_dates_col_left_dis:
        if model_type_left_dis == model:
            name_of_buttons_col_left = models_dates_col_left_dis.index(model_type_left_dis)
            return name_of_buttons_col_left

def index_finder_right_all(models_dates_col_right_all):
    for model in models_dates_col_right_all:
        if model_type_right_all == model:
            name_of_buttons_col_right = models_dates_col_right_all.index(model_type_right_all)
            return name_of_buttons_col_right

#columns for pie charts
col_model_dis1, col_model_all2 = st.columns((2))
#---2---Pie-Charts--
#'translation in' columns - left side
existing_data_left_dis = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(9, 75)), ttl=5)
size_left_dis = left_range_dis.groupby(buttons_col_of_each_model_left_dis[index_finder_left_dis(models_dates_col_left_dis)]).size()
pie_chart_left_dis = px.pie(left_range_dis, title=model_type_left_dis, values=size_left_dis, names=size_left_dis.index, height = 500, width= 550, hole=.4)
df_left_all = pd.DataFrame(size_left_dis)


#'intents' columns - right side
existing_data_right_all = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)
size_right_all = right_range_all.groupby(buttons_col_of_each_model_right_all[index_finder_right_all(models_dates_col_right_all)]).size()
pie_chart_right_all = px.pie(right_range_all, title=model_type_right_all, values=size_right_all, names=size_right_all.index, height = 500, width= 550, hole=.4)
df_right_all = pd.DataFrame(size_right_all)

with col_model_dis1:
    st.plotly_chart(pie_chart_left_dis)
with col_model_all2:
    st.plotly_chart(pie_chart_right_all)

dfcolall1, dfcolall2 = st.columns((2))
with dfcolall1:
    dfcol_left = st.dataframe(df_left_all, width=340)
with dfcolall2:
    dfcol_right = st.dataframe(df_right_all, width=340)

st.divider()
