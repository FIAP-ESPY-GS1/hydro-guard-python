# Função que verifica se há coordenadas do caminho do usuário que coincidem com zonas de risco
def check_risk_zones(user_path: list[float], risk_zones: list[float]) -> list[float]:
    cord_risks = []  # Lista para armazenar as coordenadas de risco encontradas

    # Percorre cada ponto do caminho do usuário
    for i in user_path:
        # Compara com cada ponto da lista de zonas de risco
        for j in risk_zones:
            if i == j:
                cord_risks.append(i)  # Adiciona à lista se for uma coordenada de risco

    return cord_risks  # Retorna as coordenadas que coincidem com zonas de risco


# Função principal que executa o programa
def main():
    # Caminho simulado do usuário (coordenadas)
    user_path = [100, 300, 155, 124]

    # Lista de zonas de risco conhecidas
    risk_zones = [100, 150, 200, 300]

    # Verifica quais coordenadas do usuário estão em zonas de risco
    result = check_risk_zones(user_path, risk_zones)

    # Exibe as coordenadas de risco encontradas
    print(result)


# Ponto de entrada do script
if __name__ == "__main__":
    main()
