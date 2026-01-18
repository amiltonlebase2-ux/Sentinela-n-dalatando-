import streamlit as st

# 1. ESTA LINHA MUDA O NOME NA ABA DO NAVEGADOR E NO SISTEMA
st.set_page_config(
    page_title="Fiscal Nacional", 
    page_icon="👑", 
    layout="centered"
)

# 2. ESTE BLOCO APAGA O CABEÇALHO CINZENTO E O MENU
st.markdown("""
    <style>
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho Vermelho com a Coroa */
    .brand-header {
        background: linear-gradient(135deg, #b30000 0%, #ff1a1a 100%);
        padding: 40px;
        border-radius: 0px 0px 30px 30px;
        color: white;
        text-align: center;
        margin: -60px -20px 30px -20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border-bottom: 5px solid #ffffff;
    }
    
    .crown-icon { font-size: 50px; display: block; margin-bottom: 10px; }

    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3.5em;
        background-color: #b30000;
        color: white;
        font-weight: bold;
        border: 2px solid #ffffff;
    }

    .business-card {
        background-color: #fff5f5;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #b30000;
        margin-top: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título dentro do aplicativo
st.markdown("""
    <div class="brand-header">
        <span class="crown-icon">👑</span>
        <h1 style='margin:0; font-size: 2.2em;'>FISCAL NACIONAL</h1>
        <p style='margin:0; opacity:0.9;'>Hamilton Neto - Angola</p>
    </div>
    """, unsafe_allow_html=True)

# --- DADOS ---
categorias = {
    "🎓 Concursos Públicos": {"Inscrição": 0, "Exame": 5000, "Diploma": 1500},
    "🏥 Saúde": {"Consulta Pública": 0, "Parto": 0, "Clínica Privada": 10000},
    "🏦 Bancos": {"Abertura": 0, "Depósito Mínimo": 5000, "Multicaixa": 2500},
    "✈️ Documentos": {"Passaporte": 30500, "BI Renovação": 500, "Criminal": 1500}
}

st.write("### 🔍 Consultar Valores Oficiais")
setor = st.selectbox("Escolha o Setor:", list(categorias.keys()))
servico = st.selectbox("Escolha o Serviço:", list(categorias[setor].keys()))
valor_real = categorias[setor][servico]
valor_pago = st.number_input("Valor solicitado (Kz):", min_value=0, step=500)

if st.button("ANALISAR AGORA"):
    if valor_pago > valor_real:
        st.error(f"🛑 VALOR ILEGAL! O preço oficial é {valor_real} Kz.")
    elif valor_pago == valor_real:
        st.success("✅ VALOR LEGAL")

# --- PARTE PROFISSIONAL (ONDE GANHAS DINHEIRO) ---
st.markdown("---")
st.write("### 💼 Consultoria Profissional")
st.markdown("""
    <div class="business-card">
        <p>📝 <b>Redação de Reclamação:</b> 5.000 Kz</p>
        <p>🚶 <b>Acompanhamento Presencial:</b> 15.000 Kz</p>
        <p>🏪 <b>Legalização de Empresa:</b> 30.000 Kz</p>
    </div>
    """, unsafe_allow_html=True)

link_wa = f"https://wa.me/244973806524?text=Olá%20Hamilton,%20vi%20o%20aplicativo%20Fiscal%20Nacional%20e%20quero%20contratar%20ajuda."
st.markdown(f'<a href="{link_wa}" target="_blank"><button style="background-color:#000000; color:#ffffff; height:60px; width:100%; border-radius:15px; font-weight:bold; cursor:pointer;">⭐ FALAR COM O FISCAL NO WHATSAPP</button></a>', unsafe_allow_html=True)

st.caption("Fiscal Nacional Angola © 2026")
