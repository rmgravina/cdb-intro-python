
def remover_tarefas():

    try:   
  
        with open('tarefas.txt', 'r') as f:

            tarefas = f.readlines()

        if tarefas:

            while True:
                    

                print("\nTarefas: \n")

                for i, tarefa in enumerate(tarefas):

                    print(f"{i + 1} - {tarefa}")

                tarefa_id = int(input("Escolha o número da tarefa a ser removida (ou digite 0 para voltar): "))

                if tarefa_id == 0:
                    break

                if 0 < tarefa_id <= len(tarefas):

                    tarefas.pop(tarefa_id - 1)

                    with open('tarefas.txt', 'w') as f:

                        f.writelines(tarefas)
                    
                    print("Tarefa removida com sucesso!")

                else:

                    print("Valor inválido, digite novamente.")
        
        else:
            print("Não existem tarefas cadastradas.")
            
    
    except FileNotFoundError:

        print("A base de dados ainda não foi gerada ou o caminho do arquivo está incorreto.")
    
    except ValueError:

        print("A entrada fornecida é inválida, digite o número correspondente a tarefa desejada.")



if __name__ == '__main__':
    remover_tarefas()