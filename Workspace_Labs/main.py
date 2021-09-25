
from math import exp
import streamlit as st
import pyrebase
import csv
import time
import random
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from firebase_workers import get_my_db_configs
import streaming_handlers
from streaming_handlers import MyStuffTracker,check_file_static



def app():
    
    st.header('Workspace_Lab')
    st.subheader('Track Real Time ML-Models Performance')

    check_file_static()



    workspace_name = st.text_input("Enter Workspace Name","Build-Mod")
    experiment_name = st.text_input("Enter Experiment Name","Exp-1")
    callbacks_name = st.selectbox("Select the Track Type : ",["Epochs Wise","Batches Wise"])
    track_key = st.text_input("Enter Tracking Key : ")





    if track_key:

        st.info('Now Showing Real - Time Updates : ')
        st.write("Workspace Name : {}".format(workspace_name))
        st.write("Experiment Name : {}".format(experiment_name))
        st.write("Callbacks Name : {}".format(callbacks_name))
        tracker = MyStuffTracker(workspace_name=workspace_name,experiment_name=experiment_name,track_key=track_key)

        while not tracker.is_ready:
            pass 


    dataP=r'./static_data/data.csv'


    cols_f = st.columns(2)


    my_variables = {}
    my_variables2 = {}

    with cols_f[0]:
        my_variables["placeholder" + str(1)] = st.empty()
        my_variables["placeholder" + str(2)] = st.empty()
        my_variables2["placeholder" + str(1)] = st.empty()
        my_variables2["placeholder" + str(2)] = st.empty()
    with cols_f[1]:
        my_variables["placeholder" + str(3)] = st.empty()
        my_variables["placeholder" + str(4)] = st.empty()
        my_variables2["placeholder" + str(3)] = st.empty()
        my_variables2["placeholder" + str(4)] = st.empty()




    start_button = st.empty()


    def live_chart():
        
        selected_headers = []
        time_selected_headers = [] 
        df = pd.read_csv(dataP)  

        headers_list = list(df.columns)

        for i in headers_list:
            if i not in ['epochs','avg_time','track_key','experiment_name','workspace_name','time_stamp']:
                selected_headers.append(i) 
        for i in headers_list:
            if i not in ['epochs','avg_time','track_key','experiment_name','workspace_name','time_stamp']:
                time_selected_headers.append(i)   


        for j,k in zip(range(len(selected_headers)), range(len(my_variables))):    
            fig = px.line(df,x='epochs',y=selected_headers[j],width=600, height=600)
            fig2 = px.line(df,x='avg_time',y=selected_headers[j],width=600, height=600)
            my_variables["placeholder"+str(k+1)].write(fig)

            my_variables2["placeholder"+str(k+1)].write(fig2)       
    

    sb = start_button.button('Start',key='start')

    if sb:
        
        start_button.empty()
        if st.button('Stop',key='stop'):
            pass
        
        while True:
            
            live_chart()
            time.sleep(0.3)