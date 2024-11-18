import streamlit as st

def show():
    # Título
    st.title("Conferenciador de Balanços")

    # Começo do bloco HTML para estilização personalizada
    st.markdown("<div class='columns-wrapper'>", unsafe_allow_html=True)

    # Criação das três colunas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Coluna 1")
    with col2:
        st.write("Coluna 2")
    with col3:
        st.write("Coluna 3")

    # Fim do bloco HTML
    st.markdown("</div>", unsafe_allow_html=True)