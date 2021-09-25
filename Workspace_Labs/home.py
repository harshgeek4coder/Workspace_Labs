import os
import streamlit as st

def app():
    st.write("The general idea of the project is to encapsulate general Machine Learning Model Training, it's training simulation and finally to display the inference with general Exploratory Data Analysis libraries.The user will have the ability to explore data mapping, model insights, and tracking the ML Lifecycle with a matter of simple clicks!.This progressive web app integrates the Machine Learning life cycle along with the development of model inference, which can have the ability to handle data re-collection, data selection, performing one-step EDA - which includes both statistical and visual analysis and getting results for better features selection. Moreover we have incorporated real-time tracking of analytical model training performance[Only for Deep Learning Models].")

    st.header("About Workspace Labs")
    
    

    st.markdown(
    """
    - The general idea of the project is to encapsulate general Machine Learning Model Training, it's training simulation and finally to display the inference with general Exploratory Data Analysis libraries.
    - The user will have the ability to explore data mapping, model selection, and getting the output all with a matter of simple clicks!
    - This progressive web app integrates the Machine Learning life cycle along with the development of model inference, which can have the ability to handle data re-collection, data selection, performing one-step EDA, Model selection as per use case, training, and getting results and one-click hyperparameter tuning for better features selection. 
    - Moreover we have incorporated real-time tracking of analytical model training performance[Only for Deep Learning Models].
    """
    )

    st.header("Developer By : ")

    st.write("This Application was developed under SRM MIC Fall 'bout Event' 21.")

    fc=st.columns(3)
    with fc[0]:
        st.write("Contributor : Harsh Sharma")
        Github_Link = """ <a href="https://github.com/harshgeek4coder/">Connect on Github</a> """
        st.markdown(Github_Link, unsafe_allow_html=True)

        Linkedin_Link = """ <a href="https://www.linkedin.com/in/harshsharma27">Connect on Linkedin</a> """
        st.markdown(Linkedin_Link, unsafe_allow_html=True)

    with fc[1]:
        st.write("Contributor : Devansh")
        Github_Link = """ <a href="https://github.com/devanshpratapsingh/">Connect on Github</a> """
        st.markdown(Github_Link, unsafe_allow_html=True)

        Linkedin_Link = """ <a href="https://www.linkedin.com/in/devanshps25/">Connect on Linkedin</a> """
        st.markdown(Linkedin_Link, unsafe_allow_html=True)

    with fc[2]:
        st.write("Contributor : Aman Nawaz")
        Github_Link = """ <a href="https://github.com/AmanNawazManjith">Connect on Github</a> """
        st.markdown(Github_Link, unsafe_allow_html=True)

        Linkedin_Link = """ <a href="https://www.linkedin.com/in/aman-nawaz-manjith-a528401ba/">Connect on Linkedin</a> """
        st.markdown(Linkedin_Link, unsafe_allow_html=True)


    
  