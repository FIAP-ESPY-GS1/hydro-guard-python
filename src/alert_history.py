def get_alert_history(alerts: list[str]) -> list[str]:
    return alerts[::-1]


def main():
    alerts = []

    while True:
        alert = input("Digite um alerta (ou 'sair' para encerrar): ")

        if alert.lower() == 'sair':
            break

        alerts.append(alert)

    history = get_alert_history(alerts)

    print(f"O histórico mais recente de alerta: {history}")


if __name__ == "__main__":
    main()
