import requests
import streamlit as st
from urlback import URL
import pandas as pd

# Estado inicial
if "UPLOADED" not in st.session_state:
    st.session_state["UPLOADED"] = False

# Função para upload de arquivos
def upload_files(files, repl_na=0):
    files = dict((file.name, pd.read_csv(file, low_memory=False)) if file.name.endswith('.csv') else (file.name, pd.read_excel(file)) for file in files)
    
    for df in files.values():
        df.fillna(repl_na, inplace=True)
    files = dict((k, val.to_dict()) for k, val in files.items())
    requests.post(f'{URL}/update', json={"files":files})
    return

# Carregar estilo CSS
with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Cabeçalho e título
st.title("Upload de Arquivos")
st.write("Por favor, insira seus arquivos para upload.")

# Formulário de upload
with st.form('Upload'):
    files = st.file_uploader("Insira os arquivos", accept_multiple_files=True)
    sub = st.form_submit_button("Enviar")

# Resetar estado UPLOADED se o botão for pressionado
if sub:
    st.session_state["UPLOADED"] = False

# Verificar e exibir arquivos enviados
if files:
    for file in files:
        st.write(f"**{file.name}** ({file.size} bytes)")

# Enviar arquivos
if sub and not st.session_state["UPLOADED"] and files != []:
    upload_files(files)
    st.success("Arquivos enviados com sucesso!")
    st.session_state["UPLOADED"] = True
    sub = False

# Mensagem de estado
if st.session_state["UPLOADED"]:
    st.info("Os arquivos foram enviados.")
