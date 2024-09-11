import streamlit as st
import requests
from urlback import URL

if 'email' in st.session_state:
    st.text(f"Insira o código enviado no email {st.session_state.email}:")
    st.text_input("codigo", label_visibility="collapsed", placeholder="Insira o código aqui")
    c1,_,c2 = st.columns((0.5,1.5,0.5))
    c1.button("Enviar")
    c2.button("Reenviar e-mail")
else:
    st.switch_page("pages/rec_senha.py")