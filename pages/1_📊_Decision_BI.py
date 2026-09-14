import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Décisionnel", page_icon="📊", layout="wide")

st.title("📊 Dashboard d'aide à la décision")
st.markdown("Ce tableau de bord simule l'analyse des ventes et des performances pour orienter des choix stratégiques.")

# Génération de données fictives (à remplacer par tes vraies données SQL/Pandas)
df = pd.DataFrame({
    'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'],
    'Region': ['Nord', 'Nord', 'Sud', 'Sud', 'Est', 'Est', 'Ouest', 'Ouest', 'Nord', 'Sud', 'Est', 'Ouest'],
    'CA': [12000, 15000, 11000, 18000, 22000, 20000, 25000, 27000, 30000, 32000, 35000, 42000],
    'Marge_ (%)': [25, 28, 22, 30, 35, 33, 38, 40, 42, 41, 45, 48]
})

# Sidebar pour les filtres interactifs
st.sidebar.header("Filtres dynamiques")
regions_disponibles = df['Region'].unique()
region_selectionnee = st.sidebar.multiselect("Sélectionner la/les région(s)", regions_disponibles, default=regions_disponibles)

# Filtrage du DataFrame
df_filtre = df[df['Region'].isin(region_selectionnee)]

# KPIs Principaux
col1, col2, col3 = st.columns(3)
col1.metric("Chiffre d'Affaires Total", f"{df_filtre['CA'].sum():,} €", "+12% vs N-1")
col2.metric("Marge Moyenne", f"{df_filtre['Marge_ (%)'].mean():.1f}%", "+2.3pts")
col3.metric("Volume de Mois Analysés", len(df_filtre))

st.divider()

# Graphiques Plotly
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Évolution du Chiffre d'Affaires")
    fig_ca = px.line(df_filtre, x='Mois', y='CA', color='Region', markers=True, title="CA par Mois et par Région")
    st.plotly_chart(fig_ca, use_container_width=True)

with col_g2:
    st.subheader("Analyse de la Marge")
    fig_marge = px.bar(df_filtre, x='Mois', y='Marge_ (%)', color='Region', barmode='group', title="Taux de marge par mois")
    st.plotly_chart(fig_marge, use_container_width=True)