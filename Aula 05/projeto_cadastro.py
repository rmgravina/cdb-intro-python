cadastro = set()

def adicionar_nome(nome):
    if nome in cadastro:
        print(f"O nome {nome} já está cadastrado.\n")
    
    else:
        cadastro.add(nome)
        print(f"O nome {nome} foi cadastrado com sucesso!\n")

def verificar_nomes():
    if not cadastro:
        print("A lista está vazia.")
    
    else:
        print("Nomes cadastrados:")
        for nome in cadastro:
            print(nome)

def main():

    while True:
        print("1 - Adicionar usuário")
        print("2 - Verificar usuários")
        print("3 - Sair")

        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome: ")
            adicionar_nome(nome)
        
        if opcao == 2:
            verificar_nomes()
        
        if opcao == 3:
            print("Saindo do programa, obrigado!\n")
            break


main()
