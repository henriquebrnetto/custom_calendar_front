import streamlit as st
import requests
from urlback import URL
from used_func import header

st.write("")
header()
st.write("")

st.subheader("Editar usuário:")
dados = requests.get(f'{URL}/users/{st.session_state.e_mail}', auth=(st.session_state.e_mail, st.session_state.password))
if dados.status_code == 200:
    resposta = dados.json()

    nome = resposta['user']['nome']
    email = resposta['user']['email']
    senha = resposta['user']['senha']

    nome = st.text_input("Nome: ", value=nome, key='nome')
    email = st.text_input("Email: ", value=email, key='email')
    senha = st.text_input("Senha:", value=senha, type="password", key='senha')
    
    if st.button("salvar alterações"):
        response = requests.put(f'{URL}/users/{st.session_state.user_email}', json={'nome': nome, 'email': email, 'senha':senha}, auth=(st.session_state.e_mail, st.session_state.password))
        st.session_state
        response.status_code
        if response.status_code == 200:    
            st.success('Usuário editado com sucesso')
        else:
            st.error('Erro ao editar o usuário')

