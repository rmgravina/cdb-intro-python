import streamlit as st
from controller.database import Database

db = Database()

@st.cache_data
def criar_table():
    return db.criar_tabela()
criar_table()
lista_tarefas = db.listar_tarefas()


st.title(":blue[Meu] :green[gerenciador] :blue[de] :red[Tarefas] 🤖")

st.divider()

with st.sidebar:

    opcao = st.selectbox("Escolha uma opção: ", ["Criar Tarefas", "Listar Tarefas", "Remover Tarefas"])


if opcao == "Criar Tarefas":

    tarefa = st.text_input("Insira o nome da tarefa: ")

    if st.button("⚡ Gravar"):

        db.inserir_tarefas(tarefa)

        st.write(f'A tarefa: "{tarefa}" foi registrada!!!!')

elif opcao == "Listar Tarefas":
    
    for index, i in enumerate(lista_tarefas):
        st.write(f"{index + 1} - {i[0]}")


else:
    
    lista_opcoes = [i[0] for i in lista_tarefas]

    opcoes = st.multiselect("Selecione a(s) tarefa(s):", lista_opcoes)

    if st.button("🔥 Remover"):
            
        for tarefa in opcoes:
            db.remover_tarefas(tarefa)

        st.rerun()