def broadcast_alerts(locations: list[str], messages: list[str]) -> list[str]:
    alerts = []

    if not locations or not messages:
        return alerts

    for message in messages:
        for location in locations:
            alerts.append(f"Exibindo alerta '{message}' em {location}")

    return alerts


def main():
    locations = ["Metrô", "Rodoviária", "Praça Central", "Terminal de Ônibus"]
    messages = ["Enchente no bairro A", "Deslizamento no bairro B", "Chuva forte no bairro C"]

    results = broadcast_alerts(locations, messages)

    print(results)


if __name__ == "__main__":
    main()
