
    
import streamlit as st

# CONFIGURAÇÃO SENTINELA NACIONAL V3.15
st.set_page_config(
    page_title="Sentinela Nacional V3.15", 
    page_icon="🛡️", 
    layout="centered"
)

# Estilo Visual V3.15 - Foco em Mobile e Acessibilidade
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho V3.15 */
    .v3-header {
        background: linear-gradient(135deg, #001f3f 0%, #004080 100%);
        padding: 25px;
        border-radius: 0px 0px 25px 25px;
        color: white;
        text-align: center;
        margin: -60px -20px 20px -20px;
    }
    
    .version-tag {
        background-color: #ffcc00;
        color: #001f3f;
        padding: 2px 10px;
        border-radius: 10px;
        font-size: 0.8em;
        font-weight: bold;
    }

    /* Botão de Análise */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #001f3f;
        color: white;
        font-weight: bold;
        border: 2px solid #ffcc00;
    }

    /* Bloco de Contactos (Denúncia) */
    .denuncia-box {
        background-color: #fdecea;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #f5c6cb;
        margin-top: 25px;
    }
    
    .phone-link {
        font-size: 20px;
        font-weight: bold;
        color: #d40000;
        text-decoration: none;
        display: block;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Topo do Aplicativo
st.markdown("""
    <div class="v3-header">
        <h1 style='margin:0;'>🛡️ SENTINELA NACIONAL</h1>
        <p style='margin:0;'>Consultoria Hamilton Neto</p>
        <span class="version-tag">VERSÃO 3.15 PRO</span>
    </div>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS COMPLETA ---
categorias = {
    "🎓 Concursos e Educação": {
        "Inscrição Concurso (Saúde/Educação/Polícia)": 0,
        "Inscrição FAA / Polícia Nacional": 0,
        "Transferência de Escola (Pública)": 0,
        "Certificado de Habilitações": 1500,
        "Autenticação de Diploma": 1000
    },
    "🏥 Saúde e Clínicas": {
        "Consulta Geral (Hospital Público)": 0,
        "Consulta Especialidade (Clínica Privada)": 10000,
        "Parto na Maternidade Pública": 0,
        "Cartão de Utente / Atestado Médico": 500,
        "Análises de Sangue (Média Privada)": 4500
    },
    "🏦 Bancos (Abertura de Conta)": {
        "Abertura de Conta": 0,
        "Depósito Inicial Obrigatório": 5000,
        "Cartão Multicaixa (Emissão)": 2500,
        "Extrato / Documentos": 500
    },
    "✈️ Passaporte e SME": {
        "Passaporte Ordinário": 30500,
        "Passaporte Urgente": 45000,
        "Visto de Turismo / Trabalho": 15000
    },
    "📄 BI e Registo Civil": {
        "BI (1ª Vez / Nascimento)": 0,
        "BI (Renovação ou 2ª via)": 500,
        "Assento de Nascimento": 0,
        "Divórcio por Mútuo Consentimento": 15000
    },
    "💡 Serviços e Comércio": {
        "Taxa de Lixo (ENDE)": 1500,
        "Novo Contador": 25000,
        "Alvará Comercial": 15000,
        "Ligação de Água": 18000
    }
}

# --- INTERFACE DE BUSCA ---
st.write("### 🔍 Consultar Taxa Oficial")
setor = st.selectbox("Selecione o Setor:", list(categorias.keys()))
servico = st.selectbox("Serviço ou Documento:", list(categorias[setor].keys()))

valor_real = categorias[setor][servico]
valor_pago = st.number_input("Quanto estão a cobrar? (Kz):", min_value=0, step=500)

if st.button("VERIFICAR AGORA"):
    st.markdown("---")
    if valor_pago > valor_real:
        st.error(f"🛑 **VALOR IRREGULAR!**")
        st.write(f"Para **{servico}**, o valor legal é **{valor_real} Kz**.")
        st.write(f"Diferença: **{valor_pago - valor_real} Kz** a mais.")
        if valor_real == 0: st.warning("Este serviço deve ser GRATUITO por lei!")
    elif valor_pago == valor_real:
        st.success("✅ **VALOR DENTRO DA LEALIDADE**")
    else:
        st.info(f"O valor de referência é {valor_real} Kz.")

# --- NÚMEROS DE DENÚNCIA (V3.15 DESIGN) ---
st.markdown(f"""
    <div class="denuncia-box">
        <h3 style='margin-top:0; color:#d40000;'>📢 LINHAS DE DENÚNCIA:</h3>
        <p><b>🏢 AGT (Denúncias Fiscais):</b></p>
        <a class="phone-link" href="tel:923167000">📞 923 167 000</a>
        <hr>
        <p><b>👨‍💼 CONSULTORIA HAMILTON NETO:</b></p>
        <a class="phone-link" href="tel:244973806524">📞 973 806 524</a>
    </div>
    """, unsafe_allow_html=True)

# Botão WhatsApp
msg = f"Hamilton, detetei uma cobrança ilegal no setor {setor}. Pediram {valor_pago} Kz por {servico}."
link_wa = f"https://wa.me/244973806524?text={msg.replace(' ', '%20')}"

st.markdown(f'<a href="{link_wa}" target="_blank"><button style="width:100%; height:60px; background-color:#25D366; color:white; border:none; border-radius:15px; font-weight:bold; margin-top:15px; cursor:pointer;">🟢 ENVIAR PROVA (WHATSAPP)</button></a>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray; margin-top: 30px;'>Sentinela Nacional V3.15 Pro | Angola 2026</p>", unsafe_allow_html=True)
