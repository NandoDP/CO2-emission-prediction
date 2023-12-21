import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def load_data_CO2():
    with open('model_test_data.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


df = pd.read_csv("Fuel_Consumption.csv")
data_CO2 = load_data_CO2()
model = data_CO2['model']
x_test, y_test = data_CO2['x_test'], data_CO2['y_test']


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

    n = 5
    y_prediction = model.predict(x_test[:n])
    st.subheader(f"Prédiction pour les {n} premières lignes de test :")
    for i in range(n):
        st.write(f"Ligne {i+1}: Prédiction = {y_prediction[i]:.2f} | Valeur réelle = {y_test[i]:.2f} | Erreur = {abs(y_prediction[i] - y_test[i]):.2f}")


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

