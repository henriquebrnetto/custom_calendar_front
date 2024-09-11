import requests
import streamlit as st
from config import URL
from datetime import datetime
from utils import check_not_empty, check_email

colors = ['lightslategray',] * 5
colors[1] = 'crimson'

with st.form(key="form"):
    form_data = {
        "name": st.text_input("Nome"),
        "email": st.text_input('E-mail'),
        "birth_date": st.date_input('Data de Nascimento', value=None, min_value=datetime(year=1910, month=1, day=1), max_value=datetime.today(), format="DD/MM/YYYY"),
        "job_position": st.text_input('Cargo'),
        "company": st.text_input('Empresa'),
        "psswd": st.text_input('Senha', type='password')
    }

    confirm_psswd = st.text_input('Confirmar Senha', type='password')
    sub = st.form_submit_button("Submit")

if sub:
    if form_data["psswd"] == confirm_psswd and check_not_empty(form_data) and check_email(form_data["email"]):
        form_data["birth_date"] = form_data["birth_date"].strftime("%d/%m/%Y")
        new_user = requests.post(f"{URL}/users", json=form_data)
        st.rerun()
    else:
        if form_data["psswd"] == confirm_psswd:
            st.error('Senha e confirmação de senha não conferem')
        if not check_not_empty(form_data):
            st.error('Preencha todos os campos')
        if not check_email(form_data["email"]):
            st.error('Email inválido')
