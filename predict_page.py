import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model.sav', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

def show_predict_page():
    st.title("Prédiction de la quantité de C02 émis des vehicules")

    st.write("""Quelques informations necessaires sur le vehicule.""")

    taille_moteur = st.slider("Taille du moteur", 1.0, 10.0, 2.0)
    nbr_cylindre = st.slider("Nombre de cylindres", 1, 20, 5)
    cons_carburant = st.slider("Consommation de carburant", 1.0, 50.0, 10.0)

    click = st.button("Prédire l'émission de C02")
    if click:
        input_data = np.asarray([taille_moteur, nbr_cylindre, cons_carburant]).reshape(1, -1)
        prediction = data.predict(input_data)

        st.subheader(f"La quantité de C02 émis par ce vehicule est estimer à {prediction[0]:.2f}")
    
    with st.sidebar.expander("A propos du model"):
        st.markdown("""

        Après avoir entrainer trois models de régressions avec les données 
        (voir Exploration), le model de *régression linéaire de scikit-learn* 
        semble etre légérement plus performant.

        Il offre le meilleur score **R²** avec la plus petite erreur quadratique moyenne.

        """)
