import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Portfolio | Data Analyst & BI Expert",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 1.25rem;
        color: #4B5563;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .badge {
        display: inline-block;
        padding: 0.35em 0.7em;
        font-size: 0.85rem;
        font-weight: 600;
        border-radius: 0.375rem;
        background-color: #E0E7FF;
        color: #3730A3;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    .badge-soft {
        display: inline-block;
        padding: 0.35em 0.7em;
        font-size: 0.85rem;
        font-weight: 600;
        border-radius: 0.375rem;
        background-color: #F1F5F9;
        color: #475569;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    .card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .card-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 10px;
    }
    .exp-box {
        border-left: 3px solid #3B82F6;
        padding-left: 15px;
        margin-bottom: 25px;
    }
    .exp-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1E3A8A;
    }
    .exp-company {
        font-size: 0.95rem;
        font-weight: 600;
        color: #4B5563;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER / SECTION DE PRÉSENTATION ---
col_img, col_txt = st.columns([1, 3], gap="large")

with col_img:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #3B82F6 0%, #1E3A8A 100%); width: 180px; height: 180px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 50px; font-weight: bold; box-shadow: 0 10px 15px rgba(0,0,0,0.1);">
        DA
    </div>
    """, unsafe_allow_html=True)

with col_txt:
    st.markdown('<p class="main-title">Portfolio Professionnel</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Data Analyst & Développeur Power BI | Spécialiste IA Agentic & Solutions Décisionnelles</p>',
        unsafe_allow_html=True)

    # Skills techniques sous forme de badges
    st.markdown("""
    <div>
        <span class="badge">Python</span>
        <span class="badge">DAX</span>
        <span class="badge">SQL</span>
        <span class="badge">Power BI</span>
        <span class="badge">IA Agentic</span>
        <span class="badge">n8n / Automatisation</span>
        <span class="badge">Machine Learning</span>
        <span class="badge">Data Mining</span>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Passionné par l'analyse de données, l'IA Agentic et le développement de solutions décisionnelles. 
    Mon approche méthodique, combinée à une forte capacité d'adaptation et l'intégration des agents IA, 
    me permet de répondre aux besoins spécifiques des clients tout en garantissant la qualité et la performance des solutions mises en place.
    """)

st.divider()

# --- SECTION : EXPÉRIENCES PROFESSIONNELLES & FORMATIONS (2 Colonnes) ---
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown("### 💼 Expériences Professionnelles")

    st.markdown("""
    <div class="exp-box">
        <div class="exp-title">Responsable War-room</div>
        <div class="exp-company">Yas Axian Telecom | 2024 - Aujourd'hui</div>
        <ul>
            <li>Analyse et interprétation des données pour identifier les tendances et améliorer les performances de l'entreprise.</li>
            <li>Collecte des données, mise en place des données et des tableaux de bord.</li>
            <li>Participation à la définition des objectifs stratégiques liés à l'utilisation et l'analyse des données.</li>
            <li>Collaboration avec les équipes techniques pour assurer la qualité et la fiabilité des données recueillies.</li>
        </ul>
    </div>

    <div class="exp-box">
        <div class="exp-title">Data Miner</div>
        <div class="exp-company">Yas Axian Telecom | 2022 - 2024</div>
        <ul>
            <li>Mise à jour des Dashboards (Output, intégrité des données).</li>
            <li>Rapports journaliers (Sessions de réunions, livrables).</li>
            <li>Analyse des besoins data des clients en rapport avec les besoins métiers.</li>
            <li>Pilotage des indicateurs de performance, analyse des bases de données Power BI et Data visualisation, animation des reportings projet.</li>
        </ul>
    </div>

    <div class="exp-box">
        <div class="exp-title">Data Analyste Junior</div>
        <div class="exp-company">Chambre de Commerce et d'Industrie de Nosy-Be | 2020 - 2022</div>
        <ul>
            <li>Analyse des données, prédictions des PPN, et mise en place d'opportunités d'affaires.</li>
            <li>Classifications et regroupement des différents produits à l'aide de modèles de machine learning.</li>
            <li>Collecte des données et informations requises pour analyser et améliorer les résultats d'activités.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("### 🎓 Formations & Certifications")

    st.markdown("""
    <div class="exp-box">
        <div class="exp-title">ISPM - Madagascar</div>
        <div class="exp-company">Ingénieur en Informatique de Gestion en Génie Logiciel et en Intelligence Artificielle</div>
        <p style="color: #64748B; font-size: 0.9rem; margin-top: 5px;">2014 - 2016</p>
    </div>

    <div class="exp-box">
        <div class="exp-title">ISPM - Madagascar</div>
        <div class="exp-company">Licence en Informatique de Gestion en Génie Logiciel et en Intelligence Artificielle</div>
        <p style="color: #64748B; font-size: 0.9rem; margin-top: 5px;">2011 - 2014</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📜 Certifications & Langues")
    st.markdown("""
    * **Microsoft Learn :** Conception, création de modèles sémantiques et sécurité du modèle.
    * **Langue Française :** DALF C1 • DELF B2 • DILF B1.
    * **Langue Anglaise :** Certificate in English Language (American English Course).
    """)

    st.markdown("#### 🧠 Soft Skills")
    st.markdown("""
    <div>
        <span class="badge-soft">Gestion du temps & Organisation</span>
        <span class="badge-soft">Communication & Relations interpersonnelles</span>
        <span class="badge-soft">Autonomie & Travail en équipe</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- SECTION : EXPLORER LE PORTFOLIO (Navigation interactive) ---
st.markdown("### 🚀 Explorez les modules interactifs de mon Portfolio")
st.markdown("Découvrez mes réalisations techniques à travers les différentes sections ci-dessous :")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <div class="card-title">📊 Dashboard Décisionnel</div>
        <p style="color: #64748B; font-size: 0.95rem;">Tableaux de bord interactifs (Plotly / Power BI mindset) pour piloter la croissance et analyser les KPIs.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Accéder au Dashboard", use_container_width=True):
        st.switch_page("pages/1_📊_Decision_BI.py")

with c2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🤖 Modèle Machine Learning</div>
        <p style="color: #64748B; font-size: 0.95rem;">Démonstration d'un modèle prédictif (classification/prédiction) avec interface de test en temps réel.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Tester le Modèle ML", use_container_width=True):
        st.switch_page("pages/2_🤖_Machine_Learning.py")

with c3:
    st.markdown("""
    <div class="card">
        <div class="card-title">⚙️ Automatisations n8n</div>
        <p style="color: #64748B; font-size: 0.95rem;">Présentation de pipelines d'automatisation, intégration low-code et flux de données intelligents.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Voir les Workflows n8n", use_container_width=True):
        st.switch_page("pages/3_⚙️_Automations_n8n.py")

st.divider()

# --- FOOTER ---
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("#### 📬 Me contacter")
    st.write("Ouvert aux opportunités de **Lead Data Analyst** ou de consultance en BI & IA.")
    st.write("[🔗 Mon profil LinkedIn](https://linkedin.com) | [💻 Mon GitHub](https://github.com)")

with col_f2:
    st.markdown("#### 📄 CV & Téléchargement")
    st.write("Retrouvez l'ensemble de mon parcours détaillé au format PDF.")
    # Décommente si tu ajoutes ton CV en PDF dans ton dossier GitHub
    # with open("cv.pdf", "rb") as file:
    #     st.download_button(label="📥 Télécharger mon CV", data=file, file_name="CV_Data_Analyst.pdf", use_container_width=True)