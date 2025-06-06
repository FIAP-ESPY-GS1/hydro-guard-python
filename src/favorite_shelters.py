# Menu de opções exibido ao usuário
MENU = """    =======================================
        1 - Adicionar abrigo favorito
        2 - Remover abrigo favorito
        3 - Listar favoritos
        0 - Sair
    =======================================
"""


# Função principal que gerencia os abrigos favoritos
def favorite_shelters():
    favorites = []  # Lista para armazenar os abrigos favoritos

    print(MENU)  # Exibe o menu na primeira execução

    while True:
        option = input("Digite a opção desejada: ")  # Recebe a escolha do usuário

        if option == "1":
            # Adiciona um novo abrigo à lista de favoritos
            name = input("Digite o nome do abrigo favorito: ")
            favorites.append(name)

        elif option == "2":
            # Exibe os favoritos e solicita qual será removido
            print(f"Favoritos: {favorites}")
            name = input("Digite o nome do abrigo favorito a ser removido: ")

            # Tenta remover o abrigo da lista, se existir
            if name in favorites:
                favorites.remove(name)
            else:
                print("Abrigo não encontrado na lista de favoritos.")

        elif option == "3":
            # Lista todos os abrigos favoritos
            print(f"Favoritos: {favorites}")

        elif option == "0":
            # Encerra o programa
            break

        else:
            # Informa opção inválida
            print("Opção inválida!")


# Função principal do script
def main():
    favorite_shelters()


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
