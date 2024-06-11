from utils.criar_tarefa import criar_tarefa
from utils.listar_tarefas import listar_tarefas
from utils.remover_tarefas import remover_tarefas



def main():

    print("Bem vindo ao Gerenciador de Tarefas!\n")

    while True:
        print("Escolha uma opção:\n")
        print("1 - Criar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Remover Tarefa")
        print("\nOu então digite 'sair' para encerrar o programa.")
        
        escolha = input("\nDigite a sua opção: ")

        if escolha == "1":
            criar_tarefa()
        
        elif escolha == "2":
            listar_tarefas()

        elif escolha == "3":
            remover_tarefas()
        
        elif str(escolha).lower() == 'sair':
            print("\nPrograma encerrado!")
            break

        else:
            print("Opção inválida, tente novamente..")



if __name__ == "__main__":
    main()



