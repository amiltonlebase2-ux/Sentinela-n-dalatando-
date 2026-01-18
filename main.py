import streamlit as st

st.set_page_config(page_title="Fiscal Nacional", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: red;'>👑 FISCAL NACIONAL</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'><b>Hamilton Neto - O Testamento dos Preços Oficiais</b></p>", unsafe_allow_html=True)

st.warning("⚠️ Se cobrarem mais do que está aqui, é GASOSA! Fale comigo.")

# --- 🏦 BANCOS E DEPÓSITOS ---
with st.expander("🏦 BANCOS (Depósito Inicial e Cartão)"):
    st.write("**BAI / BFA / ATLANTICO / BNI / KEVE / BIR / VTB:** 5.000 Kz")
    st.write("**BIC / SOL / BPC / BE:** 2.500 Kz")
    st.write("**STANDARD BANK:** 10.000 Kz")
    st.write("**Taxa Cartão Multicaixa:** 2.500 Kz")

# --- 💍 VIDA CIVIL E JUSTIÇA ---
with st.expander("💍 REGISTOS, DIVÓRCIO E ÓBITO"):
    st.write("**B.I. (2ª Via):** 500 Kz")
    st.write("**Passaporte:** 30.500 Kz")
    st.write("**Casamento:** 15.000 Kz")
    st.write("**Divórcio Mútuo:** 20.000 Kz")
    st.write("**Assento de Óbito:** Grátis")
    st.write("**Registo Criminal:** 1.500 Kz")
    st.write("**Custas de Tribunal:** 8.800 Kz")

# --- 🚗 TRANSPORTE E ALFÂNDEGA ---
with st.expander("🚗 TRÂNSITO E ALFÂNDEGA"):
    st.write("**Carta de Condução:** 40.050 Kz")
    st.write("**Livrete:** 15.000 Kz")
    st.write("**Título de Propriedade:** 10.000 Kz")
    st.write("**Taxa de Circulação:** 5.000 Kz")
    st.write("**Alfândega (Isenção Bagagem):** Até 1.000.000 Kz")

# --- 🏠 CASA E NEGÓCIOS ---
with st.expander("🏠 ALVARÁS, LUZ E ÁGUA"):
    st.write("**Alvará Comercial:** 25.000 Kz")
    st.write("**Ligação de Água:** 25.000 Kz")
    st.write("**Ligação de Luz:** 35.000 Kz")
    st.write("**Taxa de Lixo:** 1.500 Kz")
    st.write("**Atestado de Residência:** 500 Kz")

st.markdown("---")
st.write("### 💼 CONSULTORIA HAMILTON (2.500 Kz)")
whatsapp_link = "https://wa.me/244973806524?text=Preciso%20de%20ajuda%20Fiscal"
st.link_button("⭐ FALAR COM O FISCAL NO WHATSAPP", whatsapp_link)
