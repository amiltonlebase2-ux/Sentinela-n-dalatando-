import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Sentinela Cuanza Norte", page_icon="🛡️")

# Cabeçalho Profissional
st.title("🛡️ Sentinela de Cuanza Norte")
st.subheader("Auditor Digital de Taxas e Licenças")
st.markdown("---")

st.info("""
**Objetivo:** Verificar a legalidade de cobranças e taxas comerciais em N'dalatando. 
Proteja o seu negócio com base na Lei Geral de Taxas.
""")

# Base de Dados de Taxas (Exemplos para Angola)
banco_de_dados = {
    "Alvará Comercial (Pequeno Porte)": 15000,
    "Licença Sanitária": 12000,
    "Taxa de Higiene e Limpeza": 5000,
    "Venda Ambulante (Mensal)": 2500,
    "Taxa de Publicidade (Painel/Placa)": 8000,
    "Ocupação de Solo (m²)": 3000
}

# Interface do Usuário
st.write("### ⚙️ Configuração da Auditoria")
servico = st.selectbox("Selecione o serviço que deseja consultar:", list(banco_de_dados.keys()))

valor_cobrado = st.number_input("Introduza o valor que lhe foi solicitado (Kz):", min_value=0, step=500)

# Lógica de Verificação
valor_legal = banco_de_dados[servico]

st.markdown("---")

if st.button("VERIFICAR AGORA"):
    if valor_cobrado > valor_legal:
        diferenca = valor_cobrado - valor_legal
        st.error(f"⚠️ **VALOR ACIMA DA TABELA DETETADO!**")
        st.write(f"O valor fixado por lei para **{servico}** é de **{valor_legal} Kz**.")
        st.write(f"Estão a cobrar **{diferenca} Kz** a mais.")
        st.warning("Recomendação: Solicite a Guia de Recolha de Receitas do Estado (GRIS) oficial.")
    
    elif valor_cobrado == valor_legal:
        st.success(f"✅ **VALOR DENTRO DA LEGALIDADE**")
        st.write(f"O valor de {valor_legal} Kz está correto de acordo com a tabela oficial.")
    
    else:
        st.info("O valor introduzido é menor que a taxa padrão. Verifique se há isenção.")

# Rodapé de Autoridade
st.markdown("---")
st.caption("Desenvolvido por Amilton Marketing - Soluções Tecnológicas para Transparência")
