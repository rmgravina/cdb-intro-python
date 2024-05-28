
def criar_tarefa():
    
    entrada = input("Digite o nome da tarefa: ")

    with open('tarefas.txt', 'a') as f:
        f.write(entrada + '\n')
    
    print("Tarefa incluída com sucesso!")