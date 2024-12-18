import streamlit as st
import streamlit_authenticator as stauth
import Controllers.LoginController as LoginController

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) 

    data = LoginController.loadall()