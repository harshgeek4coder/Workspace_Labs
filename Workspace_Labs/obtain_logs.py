import streamlit as st
import pyrebase
from firebase_workers import get_config_details
import pandas as pd



def app():
    st.subheader("Post Training Logs Retrieval")
    option_type=st.selectbox("Specify type of tracking",["By Experiment","Along with Track Key"])
    if option_type=='Along with Track Key':

        workspace_name = st.text_input("Enter Workspace Name","Build-Mod")

        experiment_name = st.text_input("Enter Experiment Name","Exp-1")

        track_key = st.text_input("Enter Tracking Key : ")

        def get_firebasedb_data(workspace_name,experiment_name,track_key):
            firebase_init=pyrebase.initialize_app(get_config_details)
            logging_database = firebase_init.database()
            obt_data=logging_database.child(workspace_name).child(experiment_name).child(track_key).get()
            print(obt_data.key())
        
            print(obt_data.val())
            
            #ct=store_ids=list(obt_data.val())
            ct=list(logging_database.child(workspace_name).child(experiment_name).child(track_key).get().pyres[0].item[1].keys())
            print("Headers : ",ct)
            
            store_ids=list(obt_data.val())
            print("STORE IDS",store_ids)
            pd.DataFrame(store_ids)
        
            for i in store_ids:
                log_fetch = obt_data.val().get(i) 
                mat = dict({
                "Epoch no : " : log_fetch['epochs'],
                "Accuracy : " : log_fetch['accuracy'],
                "Loss : " : log_fetch['loss'],
                    })
                print(mat)
                
            return st.write(pd.DataFrame(obt_data.val()).T)

        if track_key:

            get_firebasedb_data(workspace_name=workspace_name,experiment_name=experiment_name,track_key=track_key)    
        
    

    

    if option_type=='By Experiment':
        workspace_name = st.text_input("Enter Workspace Name","Build-Mod")

        experiment_name = st.text_input("Enter Experiment Name","Exp-1")

        def get_firebasedb_data_with_names(workspace_name,experiment_name):
            firebase_init=pyrebase.initialize_app(get_config_details)
            logging_database = firebase_init.database()
            obt_data=logging_database.child(workspace_name).child(experiment_name).get()
            print(obt_data.key())
            temp_D = []
            temp_DS=[]
            print(obt_data.val())
            for key,val in obt_data.val().items():                
                temp_D.append(val)               
            
            for i in range(len(temp_D)):                
                for k,v in temp_D[i].items():
                    temp_DS.append(v)
                    

            ct=list(logging_database.child(workspace_name).child(experiment_name).get().pyres[0].item[1].keys())
            print("Headers : ",ct)
            print("CT 0 ",ct[0])
            
            store_ids=list(obt_data.val())
            print("STORE IDS",store_ids)
        
                
            return st.write(pd.DataFrame(temp_DS))

        if experiment_name:
            with st.spinner("This might take a while..!"):
                get_firebasedb_data_with_names(workspace_name=workspace_name,experiment_name=experiment_name)    
            
        
    
                
        