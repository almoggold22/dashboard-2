import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

st.set_page_config(
    page_title="Feedbacks Dashboard",
    layout='wide',
    initial_sidebar_state='collapsed')
st.sidebar.success("Select a Page above")

#Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)
url = 'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit'

#---API Part Up To Here----------------------------------------------------------------------------------------------------------------------------------------

#Compare Page:
#Display Title and Despcription
page_col_1, page_col_2, page_col_3, page_col_4, page_col_5, page_col_6, page_col_7, page_col_8, page_col_9 = st.columns(9)
with page_col_1:
    on = st.toggle(":blue[**Dislike**]")
if on: #on = Dislike
    with page_col_9:
        st.link_button("'Dislike' Sheet",'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit#gid=1763036692')
    st.title(":grey[Feedbacks Dashboard] - :blue[Dislike]")
    st.markdown('**Data - Tool - Dis**')
    st.markdown('')
    st.markdown('')
    #-1-Set Connection with gsheets page:
    left_chart = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(9, 75)), ttl=1)
    right_chart = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(9, 75)), ttl=1)

    #left - list of date's columns names and chosen buttons:
    models_dates_col_left = ['Translation in', 'Intents', 'Embedding', 'AI21', 'Rephrase ', 'Translation out ', 'Entire flow ', 'Score']
    buttons_col_of_each_model_left = ['Translation in buttons1', 'Intents buttons1', 'Closest questions (embedding) buttons1', 'Contextual answer (AI21) buttons1', 'Rephrase buttons1', 'Translation out buttons1', 'Entire flow buttons1', 'Score buttons1']


    col1, col2, col3 = st.columns((3))
    with col2:
        model_type = st.selectbox("**Choose Model**", models_dates_col_left)

    #Dates Range
    if model_type:
        left_chart[model_type] = pd.to_datetime(left_chart[model_type])
        today1 = conn.read(spreadsheet=url, worksheet='1710462852', usecols=list(range(1)), ttl=5)
        start_date_1 = pd.to_datetime(left_chart[model_type]).min()
        end_date_1 = pd.to_datetime(today1['today']).max()
        start_date_2 = pd.to_datetime(right_chart[model_type]).min()
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
    left_range = left_chart[(left_chart[model_type] >= date1) & (left_chart[model_type] <= date2)].copy()
    right_range = left_chart[(left_chart[model_type] >= date3) & (left_chart[model_type] <= date4)].copy()
    #------------------- Up to here Date Part

    #functions to fine the index of the relevant buttons' column and use it on pie charts:
    def index_finder_left(models_dates_col_left):
        for model in models_dates_col_left:
            if model_type == model:
                name_of_buttons_col_left = models_dates_col_left.index(model_type)
                return name_of_buttons_col_left

    #columns for pie charts
    col_model1, col_model2, col_model3, col_model4, col_model5, col_model6, col_model7, col_model8, col_model9, col_model10, col_model11, col_model12, col_model13, col_model14, col_model15, col_model16, col_model17, col_model18 = st.columns((18))
    #---2---Pie-Charts--
    #'translation in' columns - left side
    existing_data_left = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(9, 75)), ttl=5)
    size_left = left_range.groupby(buttons_col_of_each_model_left[index_finder_left(models_dates_col_left)]).size()
    pie_chart_left = px.pie(left_range, values=size_left, names=size_left.index, height = 500, width= 450, hole=.4)
    df_left_dis = pd.DataFrame(size_left)

    #'intents' columns - right side
    existing_data_right = conn.read(spreadsheet=url, worksheet='1763036692', usecols=list(range(9, 75)), ttl=5)
    size_right = right_range.groupby(buttons_col_of_each_model_left[index_finder_left(models_dates_col_left)]).size()
    pie_chart_right = px.pie(right_range, values=size_right, names=size_right.index, height = 500, width= 450, hole=.4)
    df_right_dis = pd.DataFrame(size_right)
    df_right_dis.style.bar()
    with col_model2:
        st.plotly_chart(pie_chart_left)
    with col_model13:
        st.plotly_chart(pie_chart_right)

    #dfcol1, dfcol2, dfcol3, dfcol4, dfcol5 = st.columns((5))
    #with dfcol1:
    #    dfcol_left = st.dataframe(df_left_dis, width=400)
    #with dfcol4:
    #    dfcol_right = st.dataframe(df_right_dis, width=400)

    st.divider()


else: #on = All
    #Compare Page:
    #Display Title and Despcription
    with page_col_9:
        st.link_button("'All' Sheet",'https://docs.google.com/spreadsheets/d/1kSeOTYs4XPxA2Rqb3Jz5tezwjllUmbRfBO1csTILHvE/edit#gid=1664217404')
    st.title(":grey[Feedbacks Dashboard] - :violet[All]")
    st.markdown('**Data - Tool - All**')
    st.markdown("")
    st.markdown("")

    #---API Part Up To Here----------------------------------------------------------------------------------------------------------------------------------------

    #-1-Set Connection with gsheets page:
    left_chart = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)
    right_chart = conn.read(spreadsheet=url, worksheet='1664217404', usecols=list(range(9, 75)), ttl=5)

    #left - list of date's columns names and chosen buttons:
    models_dates_col_left = ['Translation in', 'Intents', 'Embedding', 'AI21', 'Rephrase ', 'Translation out ', 'Entire flow ', 'Score']
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
    col_model1, col_model2, col_model3, col_model4, col_model5, col_model6, col_model7, col_model8, col_model9, col_model10, col_model11, col_model12, col_model13, col_model14, col_model15, col_model16, col_model17, col_model18 = st.columns((18))
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

    with col_model2:
        st.plotly_chart(pie_chart_left)
    with col_model13:
        st.plotly_chart(pie_chart_right)

    #dfcolall1, dfcolall2, dfcolall3, dfcolall4, dfcolall5 = st.columns((5))
    #with dfcolall1:
    #    dfcol_left = st.dataframe(df_left_all, width=340)
    #with dfcolall4:
    #    dfcol_right = st.dataframe(df_right_all, width=340)


    st.divider()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#new plot
empty_list_for_table_data = ['']
table_data = [empty_list_for_table_data]
#df = pd.DataFrame(dict(name = [size_left.index], num = [size_left]))
fig_1 = ff.create_table(table_data)

trace1 = go.Bar(x=size_left.index, y=size_left, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Left',
                showlegend=True,
                text=size_left)
trace2 = go.Bar(x=size_right.index, y=size_right, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Right',
                showlegend=True,
                text=size_right)

fig_1.add_traces([trace1, trace2])

fig_1.layout.margin.update({'t':75, 'l':50})
fig_1.layout.update({'title': 'Models Comparison'})
fig_1.layout.update({'height':500})
fig_1.layout.update(({'width':1100}))


fig_col1, fig_col2, fig_col3, fig_col4, fig_col5, fig_col6, fig_col7, fig_col8, fig_col9 = st.columns((9))

with fig_col2:
    fig_col2_show = st.write(fig_1)

st.divider()
