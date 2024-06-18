import sqlite3


class Database:
    def __init__(self, database="data.sqlite3"):

        self.con = sqlite3.connect(database)
        self.cursor = self.con.cursor()
        

    def criar_tabela(self):
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tarefas(nome)")
        self.con.commit()
    

    def inserir_tarefas(self, tarefa):
        self.cursor.execute("INSERT INTO tarefas (nome) VALUES (?)", (tarefa,))
        self.con.commit()


    def listar_tarefas(self):
        result = self.cursor.execute("SELECT nome FROM tarefas")

        return result.fetchall()
    

    def remover_tarefas(self, tarefa):
        self.cursor.execute("DELETE FROM tarefas WHERE nome = ?", (tarefa,))
        self.con.commit()









