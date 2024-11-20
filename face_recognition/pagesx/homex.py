import streamlit as st

def show():
    # Título
    st.title("Conferenciador de Balanços")

    # Começo do bloco HTML para estilização personalizada
    st.markdown("<div class='columns-wrapper'>", unsafe_allow_html=True)

    # Fim do bloco HTML
    st.markdown("</div>", unsafe_allow_html=True)