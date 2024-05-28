
def listar_tarefas():

    try:

        with open("tarefas.txt", 'r') as f:
            tarefas = f.readlines()

            if tarefas:
                print("\nTarefas: ")
                for i, tarefa in enumerate(tarefa):
                    print(f"{i} - {tarefa}")
        
            else:
                print("Não existem registro de tarefas.")
        
    except:
        
        print("Não foi encontrado o arquivo especificado.")