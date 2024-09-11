import requests
import streamlit as st
from config import URL
from datetime import datetime
from utils import check_not_empty, check_email

colors = ['lightslategray',] * 5
colors[1] = 'crimson'

def wholeday():
    if st.session_state.whole_day:
        return True
    return False


#CORRIGIR -----------------------------
with st.form(key="form"):
    form_data = {
        "name": st.text_input("Nome"),
        "category": st.text_input('Categoria'),
        "whole_day" : st.checkbox('Dia Inteiro', value=False, key="whole_day"),
        "start_date": st.date_input('Data de Início', min_value=datetime.today(), format="DD/MM/YYYY"),
        "start_time": st.time_input('Hora de Início', value=None),
        "end_date": st.date_input('Data de Término', min_value=datetime.today(), format="DD/MM/YYYY"),
        "end_time": st.time_input('Hora de Término', value=None),
        "repeat": st.selectbox('Repetir:', ['Nenhuma', 'Diariamente', 'Semanalmente', 'Mensalmente']) #CORRIGIR INTERAÇÃO COM REPEAT
    }
    
    sub = st.form_submit_button("Submit")

if sub:
    if not form_data['whole_day']:
        form_data["start_date"] = datetime.combine(form_data['start_date'], form_data['start_time'])
        form_data["end_date"] = datetime.combine(form_data['end_date'], form_data['end_time'])
    else:
        del form_data['start_time'], form_data['end_time']
    
    del form_data['whole_day']


    if check_not_empty(form_data):
        form_data["start_date"] = form_data["start_date"].strftime("%d/%m/%Y %H:%M")
        form_data["end_date"] = form_data["end_date"].strftime("%d/%m/%Y %H:%M")
        new_user = requests.post(f"{URL}/events", json=form_data, auth=(st.session_state.e_mail, st.session_state.password))
        st.rerun()
    else:
        st.error('Preencha todos os campos')
