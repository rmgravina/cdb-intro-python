from utils.criar_tarefa import criar_tarefa
from utils.listar_tarefas import listar_tarefas

def main():

    print("Bem vindo ao Gerenciador de Tarefas!\n")

    while True:
        print("Escolha uma opção:\n")
        print("1 - Criar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Remover Tarefa")
        print("\nOu então digite 'sair' para encerrar o programa.")
        
        escolha = input("\nDigite a sua opção: ")

        if int(escolha) == 1:
            criar_tarefa()
        
        if escolha == "2":
            listar_tarefas()

        if int(escolha) == 3:
            pass
#            remover_tarefa()
        
        if str(escolha).lower() == 'sair':
            print("\nPrograma encerrado!")
            break

        else:
            print("Opção inválida, tente novamente..")



if __name__ == "__main__":
    main()



