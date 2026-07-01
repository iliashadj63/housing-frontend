import streamlit as st
import requests

st.set_page_config(page_title="Housing API")

st.title("Prédiction de Prix Immobilier")
st.markdown("Entrez les caractéristiques du logement pour estimer sa valeur.")

# TRÈS IMPORTANT : Remplace cette URL par celle de ton API sur Codespaces
# Elle doit ressembler à https://<ton-nom>-8000.app.github.dev/predict
<<<<<<< HEAD
API_URL = "https://fictional-giggle-4gvg7q977q73j4r-8000.app.github.dev/" 
=======
API_URL = "https://legendary-space-engine-rw995wp5rj7h54rj-8000.app.github.dev" 
>>>>>>> 8b3a29fd8b92f36df3aa65f4f03d6309313642e0

# Organisation en deux colonnes pour une meilleure UI
col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input("Revenu médian (MedInc)", value=8.3)
    HouseAge = st.number_input("Âge du logement (HouseAge)", value=41.0)
    AveRooms = st.number_input("Pièces moyennes (AveRooms)", value=6.9)
    AveBedrms = st.number_input("Chambres moyennes (AveBedrms)", value=1.0)

with col2:
    Population = st.number_input("Population", value=322.0)
    AveOccup = st.number_input("Occupation moyenne (AveOccup)", value=2.5)
    Latitude = st.number_input("Latitude", value=37.88)
    Longitude = st.number_input("Longitude", value=-122.23)

# Bouton de soumission en dessous des colonnes
if st.button("Submit / Predict"):
    # Construction du payload JSON
    payload = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }
    
    # Appel à l'API via requests
    with st.spinner('Calcul en cours...'):
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                result = response.json()
                price = result.get("predicted_house_value", "Erreur")
                st.success(f"Valeur estimée : **{price}**")
            else:
                st.error(f"Erreur de l'API (Code {response.status_code}) : {response.text}")
        except Exception as e:
            st.error(f"Impossible de joindre l'API. Vérifie ton URL et assure-toi que le port sur Codespaces est en 'Public'. Détail de l'erreur : {e}")