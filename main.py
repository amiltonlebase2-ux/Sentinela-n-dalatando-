import streamlit as st

# FISCAL NACIONAL ANGOLA - VERSÃO INTEGRAL SUPREMA 2026
st.set_page_config(page_title="Fiscal Nacional", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    header {visibility: hidden;} #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    .block-container { padding-top: 1rem; }
    .stApp { background-color: #ffffff; }
    .brand-header {
        background: linear-gradient(135deg, #b30000 0%, #ff1a1a 100%);
        padding: 40px; border-radius: 0px 0px 30px 30px;
        color: white; text-align: center; margin: -60px -20px 30px -20px;
        border-bottom: 5px solid #ffffff;
    }
    .crown-icon { font-size: 50px; display: block; margin-bottom: 10px; }
    .stButton>button {
        width: 100%; border-radius: 15px; height: 3.5em;
        background-color: #b30000; color: white; font-weight: bold; border: 2px solid #ffffff;
    }
    .business-card {
        background-color: #fff5f5; padding: 20px; border-radius: 15px;
        border: 2px solid #b30000; margin-top: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="brand-header">
        <span class="crown-icon">👑</span>
        <h1 style='margin:0;'>FISCAL NACIONAL</h1>
        <p style='margin:0;'>Hamilton Neto - O Guia Oficial de Angola</p>
    </div>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS COMPLETA E ACRESCENTADA ---
categorias = {
    "🏦 Bancos e Multicaixa": {
        "Depósito Inicial (BFA/BAI/BIC/Atlântico)": 5000,
        "Depósito Inicial (SOL/BPC/BCI)": 2500,
        "Taxa de Cartão Multicaixa (Emissão)": 2500,
        "Segunda Via de Cartão": 5000
    },
    "💍 Conservatória, Família e Divórcio": {
        "Processo de Casamento": 15000,
        "Divórcio por Mútuo Consentimento": 20000,
        "Divórcio Litigioso (Custas Iniciais)": 35000,
        "União de Facto": 10000,
        "Certidão de Solteiro / Narrativa": 2500,
        "Registo de Nascimento / Óbito": 0
    },
    "✈️ Identidade e SME": {
        "B.I. (1ª Vez)": 0,
        "B.I. (Renovação / 2ª Via)": 500,
        "Passaporte Ordinário": 30500,
        "Registo Criminal": 1500,
        "Visto de Trabalho (Taxas base)": 150000
    },
    "🚗 Trânsito e Transportes (DTSER)": {
        "Emissão de Carta de Condução": 40050,
        "Renovação de Carta": 17000,
        "Livrete / Título de Propriedade": 15000,
        "Inspecção Automóvel": 10200,
        "Taxa de Circulação (Ligeiros)": 5000
    },
    "🏠 Habitação, Água e Energia": {
        "Nova Ligação de Água": 25000,
        "Nova Ligação de Energia": 35000,
        "Atestado de Residência": 500,
        "Registo Predial / Imóvel": 15000,
        "Taxas de Lixo (Mensal na fatura)": 1500
    },
    "⚖️ Justiça e Tribunais": {
        "Taxa de Justiça (Processo Cível)": 8800,
        "Procuração Pública (Notário)": 5000,
        "Reconhecimento de Assinatura": 750
    },
    "🏢 Negócios, AGT e Agro": {
        "Alvará Comercial": 25000,
        "Licença de Pesca Artesanal": 5000,
        "Guia de Abate de Gado": 2000,
        "IVA": 0.14,
        "Direitos Aduaneiros (Média)": 0.30
    },
    "🎓 Educação e Concursos": {
        "Inscrição Concurso Público": 0,
        "Exame de Admissão": 5000,
        "Diploma Universitário": 15000,
        "Certificado Ensino Médio": 1500
    },
    "🏥 Saúde": {
        "Consulta Hospital Público": 0,
        "Parto Maternidade": 0,
        "Atestado Médico": 1500,
        "Cartão de Utente": 500
    }
}

st.write("### 🔍 Consultar Valores e Taxas Oficiais")
setor = st.selectbox("Escolha a Categoria:", list(categorias.keys()))
servico = st.selectbox("Escolha o Serviço:", list(categorias[setor].keys()))
valor_real = categorias[setor][servico]

if valor_real < 1 and valor_real > 0:
    v_prod = st.number_input("Valor da Mercadoria/Imóvel (Kz):", min_value=0)
    if st.button("CALCULAR IMPOSTO"):
        st.info(f"Taxa Oficial: {valor_real*100}%. Valor a pagar: {v_prod * valor_real} Kz.")
else:
    v_pago = st.number_input("Quanto lhe pediram em mãos? (Kz):", min_value=0)
    if st.button("ANALISAR AGORA"):
        st.markdown("---")
        if
