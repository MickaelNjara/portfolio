import streamlit as st
import numpy as np

st.set_page_config(page_title="Modèle Prédictif ML", page_icon="🤖", layout="wide")

st.title("🤖 Démonstration de Modèle Prédictif")
st.markdown(
    "Testez les performances de ce modèle de Machine Learning (régression/classification) entraîné sur vos données métiers.")

# Sidebar - Paramètres d'entrée du modèle
st.sidebar.header("Paramètres d'entrée (Features)")
input_1 = st.sidebar.slider("Indicateur d'engagement client (score)", 0.0, 100.0, 50.0)
input_2 = st.sidebar.selectbox("Catégorie de produit", ["Standard", "Premium", "Entreprise"])
input_3 = st.sidebar.number_input("Ancienneté client (en mois)", min_value=1, max_value=120, value=12)


# Simulation d'un modèle (remplace ceci par ton vrai modèle chargé via pickle / joblib)
# ex: model = joblib.load('mon_modele.pkl')
def simuler_prediction(val1, val2, val3):
    coeff = 1.5 if val2 == "Premium" else (2.0 if val2 == "Entreprise" else 1.0)
    score = (val1 * 0.6 + val3 * 0.4) * coeff
    return "✅ Client Fidèle / Converti" if score > 60 else "⚠️ Risque de Churn / Non converti"


resultat = simuler_prediction(input_1, input_2, input_3)

# Affichage des résultats
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Contexte & Méthodologie")
    st.write("""
    * **Algorithme utilisé :** Random Forest / XGBoost (selon ton cas).
    * **Métrique clé :** ROC-AUC = 0.88 sur le jeu de test.
    * **Objectif métier :** Anticiper les comportements cibles pour allouer efficacement le budget marketing.
    """)

    with st.expander("Voir l'importance des variables (Feature Importance)"):
        st.bar_chart({"Engagement": 0.45, "Ancienneté": 0.30, "Catégorie Produit": 0.25})

with col2:
    st.subheader("Résultat du Modèle")
    st.info(f"Paramètres saisis :\n- Score: {input_1}\n- Catégorie: {input_2}\n- Ancienneté: {input_3} mois")

    if "Fidèle" in resultat:
        st.success(f"**Prédiction :**\n{resultat}")
    else:
        st.warning(f"**Prédiction :**\n{resultat}")