import streamlit as st

st.set_page_config(page_title="Automatisations n8n", page_icon="⚙️", layout="wide")

st.title("⚙️ Pipelines de Données & Automatisations (n8n)")
st.markdown("En tant que Lead Data Analyst, l'automatisation des flux d'acquisition de données est clé. Voici des exemples d'architectures que j'ai mises en place.")

st.info("💡 **Astuce Portfolio :** Pour chaque projet n8n, décris le problème, la source, la transformation et la destination finale.")

# Projet 1
st.subheader("1. Pipeline d'ingestion CRM vers Data Warehouse")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    * **Objectif :** Récupérer automatiquement les leads et ventes depuis HubSpot et Stripe chaque nuit.
    * **Outils :** n8n, Webhooks, API REST, PostgreSQL.
    * **Valeur ajoutée :** Suppression des exports Excel manuels, mise à jour en temps réel des tableaux de bord de direction.
    """)
with col2:
    # Si tu as une image ou un schéma de ton workflow n8n, mets-le dans ton repo et affiche-le :
    # st.image("assets/n8n_workflow_1.png", caption="Exemple de workflow n8n")
    st.code("""
[Webhook Trigger] 
       │
       ▼
[HTTP Request (HubSpot)] ──► [Data Transformation (JS)]
                                       │
                                       ▼
                             [PostgreSQL Insert/Update]
    """, language="text")

st.divider()

# Projet 2
st.subheader("2. Système d'alerte automatisé sur anomalies de données")
st.markdown("""
* **Déclencheur :** Un script Python vérifie les KPIs quotidiens. Si une baisse anormale du trafic ou du CA (> 15%) est détectée...
* **Action n8n :** Envoi immédiat d'un rapport synthétique sur un canal **Slack** dédié avec un graphique généré à la volée et notification aux équipes Ops.
""")