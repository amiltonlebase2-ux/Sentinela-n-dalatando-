
import streamlit as st

# Configuração da Página para aparecer o nome "Sentinela" no navegador
st.set_page_config(page_title="Sentinela Nacional - Hamilton Neto", page_icon="🛡️", layout="centered")

# Estilo para parecer um Aplicativo profissional
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton>button {width: 100%; border-radius: 15px; height: 3.5em; background-color: #d40000; color: white; font-weight: bold; border: none;}
    .stSelectbox, .stNumberInput {margin-bottom: 20px;}
    .stTabs [data-baseweb="tab-list"] {gap: 10px;}
    .stTabs [data-baseweb="tab"] {height: 50px; background-color: #f0f2f6; border-radius: 10px; padding: 10px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Sentinela Nacional")
st.subheader("Consultoria Hamilton Neto")
st.caption("Fiscalização de Taxas e Serviços em Angola")
st.markdown("---")

# --- GRANDE BASE DE DADOS NACIONAL ---
categorias = {
    "💡 Energia (ENDE)": {
        "Taxa de Iluminação Pública": 1000,
        "Taxa de Lixo (Doméstica)": 1500,
        "Novo Contador (Monofásico)": 25000,
        "Ligação Nova de Energia": 15000
    },
    "💧 Água (EPAL/EAS)": {
        "Ligação de Água (Nova)": 18000,
        "Consumo Mínimo Estimado": 2500,
        "Reparação de Fuga na Rua": 0
    },
    "📄 Identificação e BI": {
        "Bilhete de Identidade (1ª Vez)": 0,
        "Bilhete de Identidade (Renovação)": 500,
        "Cédula Pessoal": 0,
        "Passaporte Ordinário": 30500,
        "Registo de Nascimento": 0
    },
    "🏥 Saúde Pública": {
        "Consulta Geral (Hospital Público)": 0,
        "Cartão de Utente": 500,
        "Parto na Maternidade": 0,
        "Vacinação e Emergência": 0
    },
    "💍 Conservatória e Casamento": {
        "Casamento Civil (Taxa Normal)": 15000,
        "Registo de Propriedade (Automóvel)": 12000,
        "Certidão de Óbito": 0,
        "Escritura de Terreno": 25000
    },
    "⚖️ Comércio e Fiscalização": {
        "Alvará Comercial": 15000,
        "Licença Sanitária": 12000,
        "Taxa de Higiene e Limpeza": 5000,
        "Venda Ambulante (Mensal)": 2500
    }
}

# --- INTERFACE ---
st.write("### 🔍 O que pretendes verificar?")
setor_escolhido = st.selectbox("Selecione o Setor:", list(categorias.keys()))

servicos = categorias[setor_escolhido]
servico_escolhido = st.selectbox("Escolha o Serviço:", list(servicos.keys()))

valor_oficial = servicos[servico_escolhido]
valor_pago = st.number_input("Quanto lhe estão a cobrar? (Kz)", min_value=0, step=100)

if st.button("VERIFICAR TAXA AGORA"):
    st.markdown("---")
    if valor_pago > valor_oficial:
        st.error(f"⚠️ **VALOR EXCESSIVO DETETADO!**")
        st.write(f"Para **{servico_escolhido}**, o valor real por lei é **{valor_oficial} Kz**.")
        st.write(f"Estão a cobrar **{valor_pago - valor_oficial} Kz** a mais.")
        st.warning("Dica: Peça sempre a Guia de Receita oficial. Se não derem, é ilegal.")
    elif valor_pago == valor_oficial:
        st.success("✅ **VALOR DENTRO DA LEI**")
        st.write(f"O valor de {valor_oficial} Kz está correto.")
    else:
        st.info(f"O valor oficial é {valor_oficial} Kz. Estás a pagar menos ou é gratuito.")

# --- BOTÃO DE WHATSAPP PARA HAMILTON NETO ---
st.markdown("---")
st.write("### 📢 Denunciar ou Consultoria")
mensagem = f"Olá Hamilton Neto, estou no setor de {setor_escolhido} e pediram-me {valor_pago} Kz por {servico_escolhido}. Preciso de ajuda."
link_wa = f"https://wa.me/244973806524?text={mensagem.replace(' ', '%20')}"

st.markdown(f"""
    <a href="{link_wa}" target="_blank">
        <button style="width:100%; height:60px; background-color:#25D366; color:white; border:none; border-radius:15px; font-weight:bold; font-size:16px; cursor:pointer;">
            🟢 CONTACTAR HAMILTON NETO (WhatsApp)
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown(f"<p style='text-align: center; color: gray; margin-top: 30px;'>© 2026 Hamilton Neto - Fiscalização Independente</p>", unsafe_allow_html=True)
