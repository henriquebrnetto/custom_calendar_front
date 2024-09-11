import streamlit as st
from func import login
import requests
import pandas as pd
from config import URL
import streamlit_antd_components as sac

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

if "e_mail" not in st.session_state or "password" not in st.session_state:
    logged = "xablito"
else:
    logged = requests.get(f"{URL}/login", auth=(st.session_state.e_mail, st.session_state.password)).json()["data"]


if logged == "xablito":
    login()

st.title('CALENDÁRIO DE EVENTOS')

c1, c2, c3 = st.columns((1, 1, 1))

new_event = c1.button('Novo Evento', key='new_event')
new_user = c2.button('Novo Usuário', key='new_user')
#c3.button('Sair', key='login', on_click=lambda: st.switch_page('func.py'))

if new_event:
    st.switch_page('pages/new_event.py')
elif new_user:
    st.switch_page('pages/new_user.py')