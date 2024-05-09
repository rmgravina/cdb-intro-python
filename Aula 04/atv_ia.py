import streamlit as st
import google.generativeai as genai

# Configuração do modelo

genai.configure(api_key='INSIRA_SUA_API_KEY_AQUI')
meu_modelo = genai.GenerativeModel('gemini-pro')

# Configuração da interface

st.title("PythonAI 🐍")
st.subheader("Este é um corretor de códigos Python")
st.divider()
entrada_do_usuario = st.text_area("Insira o seu código abaixo:", height=250)

# Configuração da lógica da operação

prompt = """
Corrija o código Python abaixo.
Responda com o erro encontrado, uma proposta de solução e o snippet do código corrigido.

```python
{}
```
"""


if st.button("Corrigir ⚡"):
    
    resposta = meu_modelo.generate_content(prompt.format(entrada_do_usuario))
    st.write(resposta.text)
