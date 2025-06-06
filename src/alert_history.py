# Função que retorna o histórico de alertas na ordem reversa (mais recente primeiro)
def get_alert_history(alerts: list[str]) -> list[str]:
    return alerts[::-1]  # Usando slicing para inverter a lista


# Função principal que executa o fluxo do programa
def main():
    alerts = []  # Lista para armazenar os alertas digitados pelo usuário

    # Loop para capturar alertas até que o usuário digite "sair"
    while True:
        alert = input("Digite um alerta (ou 'sair' para encerrar): ")

        # Verifica se o usuário deseja encerrar o programa
        if alert.lower() == 'sair':
            break

        # Adiciona o alerta à lista
        alerts.append(alert)

    # Obtém o histórico de alertas em ordem reversa (últimos primeiro)
    history = get_alert_history(alerts)

    # Exibe o histórico recente
    print(f"O histórico mais recente de alerta: {history}")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
