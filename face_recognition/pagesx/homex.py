import streamlit as st

def show():
    st.markdown('<div class="logo">', unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("./img/logo.png")

        with col2:
            st.image("./img/logo.png")

        with col3:
            st.image("./img/logo.png")

    st.markdown('</div>', unsafe_allow_html=True)
