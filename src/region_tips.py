# Função que retorna uma dica de segurança com base no nome da região
def get_safety_tip(region_name: str, regions: list[str], tips: list[str]):
    count = 0  # Contador para acessar a dica correspondente

    # Percorre a lista de regiões
    for i in regions:
        if i == region_name:
            return [tips[count]]  # Retorna a dica correspondente à região encontrada
        count += 1

    # Se a região não for encontrada, retorna uma mensagem padrão
    return ["Região não encontrada."]


# Função principal do programa
def main():
    # Lista de regiões mapeadas
    regions = ["Zona Norte", "Zona Sul", "Centro"]

    # Dicas de segurança correspondentes às regiões
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos", "Use transporte público"]

    # Região informada pelo usuário
    region_name = input("Digite a região do usuário (Zona Norte, Zona Sul, Centro): ")

    # Obtém e exibe a dica de segurança para a região informada
    result = get_safety_tip(region_name, regions, tips)
    print(result)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
