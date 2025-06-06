# Função que encontra as 3 rotas mais seguras (com menor distância)
def find_safe_routes(distances: list[float] = list()) -> list[float]:
    aux = 0  # Variável auxiliar para troca de valores

    # Algoritmo de ordenação simples (bubble sort) para ordenar a lista
    for i in range(0, len(distances)):
        for j in range(i + 1, len(distances)):
            if distances[i] > distances[j]:
                aux = distances[i]
                distances[i] = distances[j]
                distances[j] = aux

    # Retorna as 3 menores distâncias, ou todas se houver menos de 3
    if len(distances) >= 3:
        return distances[0:3]
    else:
        return distances[0:len(distances)]


# Função principal que executa o programa
def main():
    # Lista com distâncias das rotas
    distances = [10.6, 10.5, 20, 30.5, 30.2, 2, 40, 50]

    # Encontra as 3 rotas mais seguras
    results = find_safe_routes(distances)

    # Exibe o resultado
    print(results)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
