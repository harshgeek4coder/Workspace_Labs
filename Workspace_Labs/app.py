import os
import streamlit as st



from multipage import MultiPage
import main,home,eda_visuals,features_eng,obtain_logs
st.set_page_config(layout="wide",page_title='Workspace_Lab')
st.header("Workspace Labs")

app = MultiPage()
app.add_page("Home",home.app)
app.add_page("EDA Visuals",eda_visuals.app)
app.add_page("Automate Feature Engineering",features_eng.app)
app.add_page("Track ML Models Real-Time",main.app)
app.add_page("Retrieve Logs",obtain_logs.app)



app.run()

