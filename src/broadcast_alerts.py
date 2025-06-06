# Função que combina mensagens de alerta com locais e retorna uma lista formatada
def broadcast_alerts(locations: list[str], messages: list[str]) -> list[str]:
    alerts = []  # Lista para armazenar os alertas gerados

    # Se a lista de locais ou mensagens estiver vazia, retorna lista vazia
    if not locations or not messages:
        return alerts

    # Para cada mensagem, combina com todos os locais
    for message in messages:
        for location in locations:
            alerts.append(f"Exibindo alerta '{message}' em {location}")

    return alerts  # Retorna a lista final de alertas formatados


# Função principal que executa o programa
def main():
    # Lista de locais onde os alertas serão exibidos
    locations = ["Metrô", "Rodoviária", "Praça Central", "Terminal de Ônibus"]

    # Lista de mensagens de alerta
    messages = ["Enchente no bairro A", "Deslizamento no bairro B", "Chuva forte no bairro C"]

    # Gera os alertas combinando cada mensagem com cada local
    results = broadcast_alerts(locations, messages)

    # Exibe o resultado completo
    print(results)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
