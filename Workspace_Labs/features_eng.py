from os import write
import pandas as pd
import numpy as np 
import streamlit as st
import sklearn
from sklearn.ensemble import ExtraTreesClassifier,ExtraTreesRegressor
import plotly.express as px


def app():
     
    st.write("\n")

 
    uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    global data
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)

    if uploaded_file:
        
        
        df=data
        st.dataframe(df)   

        get_headers = list(df.columns)

        st.header("Let's Collect Some Features :")
        x = st.multiselect("select features to train",get_headers)  
        target_var = st.selectbox("Select Target feature",get_headers) 

        if x:
            st.subheader("Get Best Features Selction : ")

            df2=df
            headers_c = list(df2.columns)
            headers_c_dts = list(df2.dtypes)
            for i,j in zip(headers_c,headers_c_dts):
                if j=='O':
                    df2[i]=df[i].astype('category').cat.codes

            
            

            model=ExtraTreesClassifier()
            model2=ExtraTreesRegressor()
            model2.fit(df[x],df[target_var])
            fto=pd.Series(model2.feature_importances_,index=x)
            mc=st.container()
            fc=st.columns(2)
            with mc:
                with fc[0]:
                    st.write(df2.corr()[target_var])
                with fc[1]:           
                    st.bar_chart(fto.nlargest(5))

            st.subheader("Missing Values Handling")
            mc2=st.container()
            fc2=st.columns(2)

            with mc2:
                with fc2[0]:
                    st.write(df.isnull().sum())
                    st.write(df.notnull().sum())
                    
                with fc2[1]:

                    st.bar_chart(df.isnull().sum())               
                    st.bar_chart(df.notnull().sum())
                    

            
            
            

            
