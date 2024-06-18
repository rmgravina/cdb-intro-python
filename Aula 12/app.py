import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from st_pages import Page, show_pages, add_page_title
import os
from controller.database import Database

# configs iniciais
load_dotenv()
minha_chave = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=minha_chave)
db = Database()



show_pages(
    [
        Page("app.py", "TaskAI", "⚡"),
        Page("pages\gerenciador_de_tarefas.py", "Gerenciador de Tarefas", "🗃️"),
    ]
)



st.title("TasksAI 🤖")
st.divider()

st.subheader("Pergunte ao modelo sobre suas tarefas!")

input = st.text_area("Faça uma pergunta:", placeholder="Ex. Quantas tarefas eu tenho?")

tarefas = db.listar_tarefas()

prompt = """
Eu tenho um banco de dados com as seguintes tarefas:

{}

Responda a pergunta a seguir, levando em consideração as tarefas mencionadas.

Pergunta:

{}
"""

if st.button("Perguntar ⚡"):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt.format(tarefas, input)}
  ]
)

    st.write(completion.choices[0].message.content)

    print(prompt.format(tarefas, input))