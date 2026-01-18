
import streamlit as st

# CONFIGURAÇÃO OFICIAL - FISCAL NACIONAL ANGOLA
st.set_page_config(
    page_title="Fiscal Nacional Angola", 
    page_icon="🛡️", 
    layout="centered"
)

# Estilo para esconder cabeçalhos e menus do sistema (Design Profissional)
st.markdown("""
    <style>
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho Nacional */
    .nacional-header {
        background: linear-gradient(135deg, #001f3f 0%, #004080 100%);
        padding: 35px;
        border-radius: 0px 0px 30px 30px;
        color: white;
        text-align: center;
        margin: -60px -20px 30px -20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3.8em;
        background-color: #001f3f;
        color: white;
        font-weight: bold;
        border: 2px solid #ffcc00;
        font-size: 18px;
    }

    .denuncia-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #001f3f;
        margin-top: 30px;
    }
    
    .phone-number {
        font-size: 24px;
        font-weight: bold;
        color: #d40000;
        text-decoration: none;
        display: block;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Nacional
st.markdown("""
    <div class="nacional-header">
        <h1 style='margin:0; font-size: 2.2em;'>🛡️ FISCAL NACIONAL</h1>
        <p style='margin:5px; opacity:0.9;'><b>Angola Transparente | Consultoria Hamilton Neto</b></p>
        <div style='background:#ffcc00; color:#001f3f; display:inline-block; padding:2px 15px; border-radius:10px; font-weight:bold; font-size:0.8em;'>PRO V3.20</div>
    </div>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS NACIONAL ---
categorias = {
    "🎓 Concursos e Educação": {
        "Inscrição em Concurso Público": 0,
        "Inscrição Polícia / FAA": 0,
        "Transferência de Escola (Pública)": 0,
        "Certificado de Habilitações": 1500,
