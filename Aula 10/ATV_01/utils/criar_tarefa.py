

def criar_tarefa():
    
    while True:
            
        entrada = input("Digite o nome da tarefa (ou digite 0 para voltar): ")

        if entrada == "0":
            break

        with open('tarefas.txt', 'a') as f:
            f.write(entrada + '\n')
        
        print("Tarefa incluída com sucesso!")