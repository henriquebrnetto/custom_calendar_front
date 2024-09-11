import streamlit as st
import requests
from urlback import URL
import time


if 'email' not in st.session_state:
    st.session_state.email = ''

if 'codigo' not in st.session_state:
    st.session_state.codigo = ''

if 'env_cod' not in st.session_state:
    st.session_state.env_cod = False

if 'response_email' not in st.session_state:
    st.session_state.response_email = ''

if 'env_cod' not in st.session_state:
    st.session_state.env_cod = False

if 'response_code' not in st.session_state:
    st.session_state.response_code = False

def set_email(email):
    st.session_state.email = email
    return

def make_true_env_cod():
    st.session_state.env_cod = True
    return

def make_true_response_code():
    st.session_state.response_code = True
    return

st.subheader("Insira seu e-mail:")
_,c,_ = st.columns(3)
st.session_state.email = st.text_input('email', label_visibility="collapsed", placeholder="exemplo@gmail.com")

if st.button("Enviar e-mail de recuperação", disabled=not(bool(st.session_state.email)), on_click=set_email, args=(st.session_state.email,)):
    try:
        st.session_state.response_email = requests.get(f"{URL}/users/recuperar_senha/{st.session_state.email}").json()
    except:
        st.error("erro aao enviar email, erro:500")

if st.session_state.response_email:
    if 'sucesso' in st.session_state.response_email['mensagem']:
        st.text("")
        st.text("")
        st.text(f"Insira o código enviado no email {st.session_state.email}:")
        st.session_state.codigo = st.text_input("codigo", label_visibility="collapsed", placeholder="Insira o código aqui")
        c1,_,c2 = st.columns((0.5,1.5,0.5))
        c1.button("Enviar", on_click=make_true_env_cod)

        if c2.button("Reenviar e-mail"):
            try:
                response = requests.get(f"{URL}/users/recuperar_senha/{st.session_state.email}").json()
            except:
                st.error("erro ao enviar email, erro:500")
    else:
        st.error("e-mail inválido ou não encontrado")

if st.session_state.env_cod:
    # requests.get(f"{URL}/users/recuperar_senha/{st.session_state.email}/{st.session_state.codigo}")
    try:
        st.session_state.response_code = 1 if requests.get(f"{URL}/users/recuperar_senha/{st.session_state.email}/{st.session_state.codigo}") else 2
    except:
        st.error("Erro na requisição 1")

if st.session_state.response_code == 1:
    nova_senha = st.text_input("nova_senha", label_visibility="collapsed", placeholder="Nova senha...", type="password")
    if st.button("Mudar senha", disabled=not(nova_senha)):
        
        # try:
        #     response = requests.put(f"{URL}/users/recuperar_senha/{st.session_state.email}/{st.session_state.codigo}", json={"senha":nova_senha})
        # except:
        #     st.error("Erro na requisição 2")

        response = requests.put(f"{URL}/users/recuperar_senha/{st.session_state.email}/{st.session_state.codigo}", json={"senha":nova_senha})

        if response:
            st.success("Senha alterada com sucesso! você será redirecionado à página de login")
            time.sleep(5)
            st.switch_page("pages/login.py")
        else:
            st.error("Erro ao cadastrar a nova senha (não autorizado)")

if st.session_state.response_code == 2:
    st.error("Código inválido")