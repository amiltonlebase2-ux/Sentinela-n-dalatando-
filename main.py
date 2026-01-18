
import streamlit as st

# Configuração para parecer um aplicativo de telemóvel
st.set_page_config(page_title="Sentinela Cuanza Norte", page_icon="🛡️", layout="centered")

# Visual profissional (Azul e Branco)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton>button {width: 100%; border-radius: 12px; height: 3.5em; background-color: #004a99; color: white; font-weight: bold; border: none;}
    .stTabs [data-baseweb="tab-list"] {gap: 10px;}
    .stTabs [data-baseweb="tab"] {height: 50px; white-space: pre-wrap; background-color: #f0f2f6; border-radius: 10px; padding: 10px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Sentinela Cuanza")
st.subheader("Consultoria Hamilton Neto")
st.caption("Apoio ao Comerciante de N'dalatando")

# Abas organizadas
tab1, tab2 = st.tabs(["📊 Calculador de Taxas", "📢 Falar com Hamilton"])

with tab1:
    st.write("### Verificar Valor da Taxa")
    
    # Tabela de preços de Cuanza Norte
    taxas = {
        "Alvará Comercial": 15000,
        "Licença Sanitária": 12000,
        "Taxa de Higiene": 5000,
        "Venda Ambulante": 2500,
        "Publicidade": 8000
    }
    
    opcao = st.selectbox("Selecione o documento:", list(taxas.keys()))
    valor_pago = st.number_input("Quanto te cobraram? (Kz)", min_value=0, step=500)
    
    valor_real = taxas[opcao]
    
    if st.button("ANALISAR AGORA"):
        if valor_pago > valor_real:
            st.error(f"⚠️ ATENÇÃO: Estão a cobrar {valor_pago - valor_real} Kz a mais!")
            st.info(f"O preço oficial para {opcao} é {valor_real} Kz.")
        elif valor_pago == valor_real:
            st.success("✅ VALOR CORRETO: Esta taxa está dentro da lei.")
        else:
            st.warning("O valor está abaixo do normal. Verifique se o documento é autêntico.")

with tab2:
    st.write("### 📞 Linha Direta")
    st.write("Tens uma denúncia ou precisas de consultoria? Clica no botão abaixo para falar diretamente comigo.")
    
    # Mensagem personalizada para o teu WhatsApp
    msg_wa = f"Olá Hamilton Neto, estou a usar o site Sentinela e gostaria de uma ajuda sobre a taxa de {opcao}."
    link_wa = f"https://wa.me/244973806524?text={msg_wa.replace(' ', '%20')}"
    
    st.markdown(f"""
        <a href="{link_wa}" target="_blank">
            <button style="width:100%; height:60px; background-color:#25D366; color:white; border:none; border-radius:15px; font-weight:bold; font-size:18px; cursor:pointer;">
                🟢 FALAR COM HAMILTON NETO
            </button>
        </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"<p style='text-align: center;'><b>© 2026 Hamilton Neto - N'dalatando</b></p>", unsafe_allow_html=True)
