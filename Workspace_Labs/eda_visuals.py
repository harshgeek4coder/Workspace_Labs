
import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px

import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns


def app():

    st.markdown("## Upload Data")

    
    st.markdown("### Upload a CSV file.") 
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
        
  
        col = list(df.columns)

            
        st.subheader('Scatter Plot')
        option_x = st.selectbox(
                'What feature do you want in the x-axis?',
                    col,key=1)

        st.write('You selected:', option_x)


        option_y = st.selectbox(
               'What feature do you want in the y-axis?',
                    col)

        st.write('You selected:', option_y)

        figs=px.scatter(df,x=option_x,y=option_y)
        st.write(figs)
        

        print(list(df.columns))



        # /**************Line Plot****************/

        st.subheader('Line Plot')
        line_x = st.selectbox(
        'What feature do you want in the x-axis?',
            col)
        st.write('You selected:', line_x)
        line_y = st.selectbox(
        'What feature do you want in the y-axis?',
            col,key=2)
        st.write('You selected:', line_y)



        chart_data = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['line_x', 'line_y'])

        st.line_chart(chart_data)


        # /******************Bar chart **************/

        st.subheader('Bar Chart')
        bar_x = st.selectbox('What feature do you want in the x-axis?',
            col,key=3
        )

        fig_bar=px.histogram(df,x=bar_x)
       

        st.write(fig_bar)
        


        # /**************** Strip plot *******************/
        st.subheader('Strip Plot')
        strip_x = st.selectbox("What feature do you want in the x-axis?",
            col,key=4)
        strip_y = st.selectbox("What feature do you want in the y-axis?",
            col,key=5)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        sns.stripplot(x=df[strip_x], y=df[strip_y])
        st.pyplot()


        # /**************** Histogram *******************/
        st.subheader('Histogram')
        hist_x = st.selectbox("What feature do you want in the x-axis?",
            col,key=6)
        plt.hist(df[hist_x])
        st.pyplot()

        # /**************** Heat-map *******************/
        # st.subheader('Heatmap')

        # heat_x = st.selectbox("What feature do you want in the x-axis?",
        #     col,key=7)
        # heat_y = st.selectbox("What feature do you want in the y-axis?",
        #     col,key=8)
            
        # plt.figure(figsize=(14,7))                                    #harsh

        # sns.heatmap(data=df, annot=True)
        # plt.xlabel(heat_x)
        # st.pyplot()


        

        # /****************  Joint plot (kind='hex')**************** /
        st.subheader('Joint Plot')
        joint_x = st.selectbox("What feature do you want in the x-axis?",
            col,key=11)
        joint_y = st.selectbox("What feature do you want in the y-axis?",
            col,key=12)
        sns.jointplot(x=joint_x, y=joint_y, data=df, size=5)
        st.pyplot()




                


                