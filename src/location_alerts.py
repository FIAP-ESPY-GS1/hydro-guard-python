# Função que verifica se a coordenada do usuário está próxima de zonas de risco de enchente
def check_flood_alert(risk_coordinates: list[float], user_coord: float) -> str:
    for risk_coord in risk_coordinates:
        # Se estiver a até 10 unidades de uma zona de risco, alerta de perigo iminente
        if risk_coord - 10 <= user_coord <= risk_coord + 10:
            return "🔴 Perigo iminente de enchente! Evacue imediatamente."

        # Se estiver a até 30 unidades, mas fora da zona crítica, alerta de atenção
        if risk_coord - 30 <= user_coord <= risk_coord + 30:
            return "🟡 Área próxima a zona de risco de enchente. Fique em alerta."

    # Se não houver nenhuma zona de risco próxima
    return "🟢 Você está em uma área segura. Nenhum risco próximo detectado."


# Função principal que executa o programa
def main():
    # Coordenadas simuladas de zonas de risco
    risk_coordinates = [-105.8, -23.5, -35.4, -23.4, 50.1, 120.5, 65.2, -30]

    # Solicita a coordenada do usuário
    user_coord = float(input("Digite coordenada do usuário: "))

    # Verifica a proximidade com zonas de risco
    result = check_flood_alert(risk_coordinates, user_coord)

    # Exibe o resultado da verificação
    print(result)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
