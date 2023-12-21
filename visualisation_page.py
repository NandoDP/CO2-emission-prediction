import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv("Fuel_Consumption.csv")

def show_vizualisation_page_CO2():
    st.title("Visualiser l'évolution de la quantité de CO2 émis")

    st.write(
        """
    #### (A) Quantité CO2 émis en moyenne par rapport au nombre de cylindre
    """
    )

    data = df.groupby(["CYLINDERS"])["CO2EMISSIONS"].mean().sort_values(ascending=True)
    st.bar_chart(data, y="CO2EMISSIONS")

    st.write(
        """
    #### (B) Quantité CO2 émis en moyenne par rapport à la taille du moteur
    """
    )

    data_1 = df.groupby(["ENGINESIZE"])["CO2EMISSIONS"].mean().sort_values(ascending=True)
    st.line_chart(data_1, y="CO2EMISSIONS")

    st.write(
        """
    #### (C) Quantité CO2 émis en moyenne par rapport à la consommation de carburant
    """
    )

    data_2 = df.groupby(["FUELCONSUMPTION_COMB"])["CO2EMISSIONS"].mean().sort_values(ascending=True)
    st.line_chart(data_2, y="CO2EMISSIONS")

df_iphone = pd.read_csv("iphone_purchase_records.csv")

def show_vizualisation_page_iphone():
    st.title("Visualisation sur l'achat de iphones")

    st.write(
        """
    #### (A)  Nombre d'achat d'iphone  en fonction du genre
    """
    )

    st.bar_chart(df_iphone, x="Gender", y="Purchase Iphone")

    st.write(
        """
    #### (B)  Matrice de correlation du model KNN sur les données test.
    """
    )

    st.image('output.png', caption='Matrice de correlation')


    # fig, ax = plt.subplots()
    # sns.heatmap(df_iphone.drop('Gender', axis=1).corr(), ax=ax)
    # st.write(fig)