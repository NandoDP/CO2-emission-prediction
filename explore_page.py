import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
# from predict_page import model_test_data

df = pd.read_csv("Fuel_Consumption.csv")


def show_explore_page_CO2():
    st.title("Explorer les données d’entrainement.")

    st.write(
        """
    #### Appercu des données d'entrainement du model
    """
    )
    st.write(f"Dimensions : {df.shape}")
    st.dataframe(df.head())
    st.write("La description du dataFrame:")
    st.write(df.describe())

    # Prediction de quelques valeurs des données test
    with open('model_test_data.pkl', 'rb') as file:
        model_test_data = pickle.load(file)

    model = model_test_data['model']    
    x_test = model_test_data['x_test']
    y_test = model_test_data['y_test']
    n = 5
    y_pred_n = model.predict(x_test[:n])
    st.write(f"""#### Prédiction pour les {n} premières lignes des données test :""")
    for i in range(n):
        # st.write(f'{y_pred_n[i]:.2f} -- {y_test[i]}')
        st.write(f"Ligne  {i+1}:  Prédiction  =  {y_pred_n[i]:.2f}  --  Valeur réelle  =  {y_test[i]}  --  Erreur  =  {abs(y_pred_n[i] - y_test[i]):.2f}")

df_iphone = pd.read_csv("iphone_purchase_records.csv")

def show_explore_page_iphone():
    st.title("Explorer les données d’entrainement.")

    st.write(
        """
    #### Appercu des données d'entrainement du model
    """
    )
    st.write(f"Dimensions : {df_iphone.shape}")
    st.dataframe(df_iphone.head())
    st.write("La description du dataFrame:")
    st.write(df_iphone.describe())

