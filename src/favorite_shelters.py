def favorite_shelters():
    favorites = []
    while True:
        menu = """    =======================================
        1 - Adicionar abrigo favorito
        2 - Remover abrigo favorito
        3 - Listar favoritos
        0 - Sair
    =======================================
        """

        option = input(menu)

        if option == "1":
            name = input("Digite o nome do abrigo favorito: ")
            favorites.append(name)

        elif option == "2":
            print(f"Favoritos: {favorites}")
            name = input("Digite o nome do abrigo favorito a ser removido: ")
            favorites.remove(name)

        elif option == "3":
            print(f"Favoritos: {favorites}")

        elif option == "0":
            break

        else:
            print("Opção inválida!")



def main():
    favorite_shelters()


if __name__ == "__main__":
    main()
