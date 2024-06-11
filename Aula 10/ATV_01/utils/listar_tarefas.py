
def listar_tarefas():

    try:

        with open("tarefas.txt", 'r') as f:
            tarefas = f.readlines()

            if tarefas:
                print("\nTarefas: \n")
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1} - {tarefa}")
        
            else:
                print("Não existem registro de tarefas.")
        
    except:
        
        print("Não foi encontrado o arquivo especificado.")