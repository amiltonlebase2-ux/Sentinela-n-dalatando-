import streamlit as st

# Deixa a página compacta e ajustada ao telemóvel
st.set_page_config(page_title="Sentinela", page_icon="🛡️", layout="centered")

# CSS para esconder menus desnecessários e melhorar botões
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stButton>button {width: 100%; border-radius: 10px; height: 3em; background-color: #007bff; color: white;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Sentinela Cuanza")
st.caption("Versão 1.0 - Apoio ao Comércio Local")

# Menu em abas (mais pequeno e organizado)
aba1, aba2 = st.tabs(["📊 Auditor", "📞 Denúncia"])

with aba1:
    st.write("### Verificar Taxa")
    servico = st.selectbox("Serviço:", [
        "Alvará Comercial", "Licença Sanitária", 
        "Taxa de Higiene", "Venda Ambulante", "Publicidade"
    ])
    
    valor_legal = {"Alvará Comercial": 15000, "Licença Sanitária": 12000, "Taxa de Higiene": 5000, "Venda Ambulante": 2500, "Publicidade": 8000}
    
    cobrado = st.number_input("Valor solicitado (Kz):", min_value=0, step=500)
    
    if st.button("CALCULAR AGORA"):
        legal = valor_legal[servico]
        if cobrado > legal:
            st.error(f"Excesso de: {cobrado - legal} Kz")
            st.warning(f"O valor fixado é {legal} Kz.")
        elif cobrado == legal:
            st.success("Valor Correto!")
        else:
            st.info("Valor abaixo do padrão.")

with aba2:
    st.write("### Linha de Apoio")
    st.info("Caso detete uma irregularidade, contacte as autoridades ou use o botão abaixo:")
    
    texto_denuncia = f"Olá, gostaria de reportar uma irregularidade na taxa de {servico} em N'dalatando."
    # Link direto para o teu WhatsApp (muda o número abaixo pelo teu)
    st.markdown(f"[📢 Enviar Alerta via WhatsApp](https://wa.me/244973806524?text={texto_denuncia})")

st.markdown("---")
st.caption("© 2026 Amilton Neto - N'dalatando")
