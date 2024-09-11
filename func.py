import streamlit as st
import streamlit_antd_components as sac
import requests
from config import URL

def pagina_login():
    _,c2,_ = st.columns((0.3, 1, 0.3))

    c2.write("")
    c2.image('images\JJ.png', width=400)
    sac.divider(align='center', color='red', key='key')


@st.dialog("Fazer Login")
def login():

    st.write("")
    st.subheader('Login:')
    st.session_state.e_mail = st.text_input('email:', key='email')
    st.session_state.password = st.text_input('Senha: ', type='password', key='senha')
    st.write("")

    col1, _, col2 = st.columns([0.7, 0.8, 0.7])
    with col1:
        if st.button('cadastre-se', key='cadastre-se'):
            st.switch_page('pages/cadastro.py')

    not_logged = False
    with col2:
        if st.button('Entrar', key='entrar'):
            response = requests.get(f"{URL}/login", auth=(st.session_state.e_mail, st.session_state.password))
            if response.status_code == 200:
                st.switch_page('app.py')
            else:
                not_logged = True

    if not_logged:
        st.error("Erro ao fazer login. Verifique suas credenciais.")

    st.write("")

    _,c,_ = st.columns((0.5,1,0.5))

    if c.button("Esqueci minha senha"):
        st.switch_page("pages/rec_senha.py")