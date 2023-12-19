import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page, show_vizualisation_page

# page = st.sidebar.selectbox('Prédire, explorer ou visualiser', ('Prédiction', 'Exploration', 'Visualisation'))
page = st.sidebar.radio('Sommaire :', ('Prédiction', 'Exploration', 'Visualisation'))


if page == 'Prédiction':
    show_predict_page()
elif page == 'Exploration':
    show_explore_page()
else:
    show_vizualisation_page()
