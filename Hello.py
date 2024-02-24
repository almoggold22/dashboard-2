import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px

st.title(":grey[All Models -] :violet[Dis]")

#Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)
url = 'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit'


col1, col2, col3 = st.columns((3))
##'translation_in' columns
translation_in_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(10, 18)), ttl=5)
size_translation_in = translation_in_all.groupby('Translation in buttons1').size()
date_translation_in = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(10)), ttl=5)
pie_chart_translation_in = px.pie(date_translation_in, title='Translation In', values=size_translation_in, names=size_translation_in.index, height = 400, width= 350, hole=.4)
#fig_translation_in = pie_chart_translation_in.update_layout(legend=dict(orientation="h"))

with col1:
    pie1 = st.write(pie_chart_translation_in)
    
##'intents' columns
intents_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(19, 27)), ttl=5)
size_intents = intents_all.groupby('Intents buttons1').size()
date_intents = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(19)), ttl=5)
pie_chart_intents = px.pie(date_intents, title='Intents', values=size_intents, names=size_intents.index, height = 400, width= 350, hole=.4)
#fig_intents = pie_chart_intents.update_layout(legend=dict(orientation="h"))

with col2:
    pie2 = st.write(pie_chart_intents)

##'Closest questions (embedding)' columns
embedding_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(28, 36)), ttl=5)
size_embedding = embedding_all.groupby('Closest questions (embedding) buttons1').size()
date_embedding = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(28)), ttl=5)
pie_chart_embedding = px.pie(date_embedding, title='Embedding', values=size_embedding, names=size_embedding.index, height = 400, width= 500, hole=.4)
#fig_embedding = pie_chart_embedding.update_layout(legend=dict(orientation="h"))

with col3:
    pie3 = st.write(pie_chart_embedding)

col4, col5, col6 = st.columns((3))
##'Contextual answer (AI21)' columns
ai21_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(37, 45)), ttl=5)
size_ai21 = ai21_all.groupby('Contextual answer (AI21) buttons1').size()
date_ai21 = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(37)), ttl=5)
pie_chart_ai21 = px.pie(date_ai21, title='AI21', values=size_ai21, names=size_ai21.index, height = 400, width= 350, hole=.4)
#fig_ai21 = pie_chart_ai21.update_layout(legend=dict(orientation="h"))

with col4:
    pie4 = st.write(pie_chart_ai21)

##'Rephrase' columns
rephrase_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(46, 54)), ttl=5)
size_rephrase = rephrase_all.groupby('Rephrase buttons1').size()
date_rephrase = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(46)), ttl=5)
pie_chart_rephrase = px.pie(date_rephrase, title='Rephrase', values=size_rephrase, names=size_rephrase.index, height = 400, width= 350, hole=.4)
#fig_rephrase = pie_chart_rephrase.update_layout(legend=dict(orientation="h"))

with col5:
    pie5 = st.write(pie_chart_rephrase)

##'Translation Out' columns
translation_out_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(55, 63)), ttl=5)
size_translation_out = translation_out_all.groupby('Translation out buttons1').size()
date_translation_out = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(55)), ttl=5)
pie_chart_translation_out = px.pie(date_translation_out, title='Translation Out', values=size_translation_out, names=size_translation_out.index, height = 400, width= 350, hole=.4)
#fig_translation_out = pie_chart_translation_out.update_layout(legend=dict(orientation="h"))

with col6:
    pie6 = st.write(pie_chart_translation_out)

##'Entire Flow' columns
entire_flow_all = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(64, 72)), ttl=5)
size_entire_flow = entire_flow_all.groupby('Entire flow buttons1').size()
date_entire_flow = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(64)), ttl=5)
pie_chart_entire_flow = px.pie(date_entire_flow, title='Entire Flow', values=size_entire_flow, names=size_entire_flow.index, height = 400, width= 350, hole=.4)
#fig_entire_flow = pie_chart_entire_flow.update_layout(legend=dict(orientation="h"))

col7, col8 = st.columns((2))
with col7:
    pie7 = st.write(pie_chart_entire_flow)

st.divider()
