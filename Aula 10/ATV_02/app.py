import streamlit as st
import sqlite3

st.title(":blue[Meu] :green[gerenciador] :blue[de] :red[Tarefas] 🤖")

st.divider()

with st.sidebar:

    opcao = st.selectbox("Escolha uma opção: ", ["Criar Tarefas", "Listar Tarefas", "Remover Tarefas"])


if opcao == "Criar Tarefas":

    tarefa = st.text_input("Insira o nome da tarefa: ")

    if st.button("⚡ Gravar"):

        st.write(f'A tarefa: "{tarefa}" foi registrada!!!!')