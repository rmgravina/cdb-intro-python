# Introdução à Programação com Python

<p align="center">
  <img src="misc\logo_cdb_python.png" width="300"/>
</p>

Este repositório contém arquivos com conteúdo e exercícios práticos para o curso de Introdução à Programação com Python.

O curso é promovido pela plataforma [Códigos do Bem](https://codigosdobem.com.br/) e tem como objetivo ensinar os conceitos básicos de programação utilizando a linguagem Python.

# Guia de Instalação e Uso

Este repositório contém arquivos Jupyter Notebook (`.ipynb`) que podem ser clonados e executados em sua máquina local. Siga as instruções abaixo para configurar o ambiente e executar os notebooks.

## Clonando o Repositório

Você pode clonar este repositório utilizando o comando `git clone` em seu terminal ou prompt de comando:

```bash
git clone https://github.com/rmgravina/cdb-intro-python.git
```


## Configurando o Ambiente

Antes de executar os notebooks, é necessário configurar o ambiente Python e instalar as dependências. Recomenda-se a utilização de um ambiente virtual para evitar conflitos com outras bibliotecas instaladas em seu sistema. Siga os passos abaixo:

1. **Instale o Python**: Se ainda não tiver o Python instalado, faça o download e a instalação a partir do [site oficial](https://www.python.org/downloads/).

2. **Crie um Ambiente Virtual (opcional)**: Abra um terminal ou prompt de comando e execute o seguinte comando para criar um ambiente virtual:

    ```
    python -m venv myenv
    ```

    Substitua `myenv` pelo nome desejado para o ambiente virtual.

3. **Ative o Ambiente Virtual (opcional)**: Dependendo do seu sistema operacional, o comando para ativar o ambiente virtual pode variar:

    - No Windows:
        ```
        myenv\Scripts\activate
        ```

    - No macOS e Linux:
        ```
        source myenv/bin/activate
        ```

4. **Instale as Dependências (quando aplicável)**: No diretório raiz do repositório clonado, execute o seguinte comando para instalar as dependências:

    ```
    pip install -r requirements.txt
    ```

## Executando os Notebooks

Após configurar o ambiente, você pode executar os notebooks `.ipynb` utilizando o próprio VSCode, através da instalação da extensão `Jupyter` e `Python`. Basta abrir o notebook desejado e clicar no botão de execução para rodar as células de código.

## Contribuindo

Se encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request. Sua contribuição é muito bem-vinda!


