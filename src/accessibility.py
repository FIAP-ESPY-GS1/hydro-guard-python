# Função que simula a "fala" de alertas, retornando palavras separadas dos alertas
def speak_alerts(alerts: list[str], is_enabled: bool) -> list[str]:
    # Se a acessibilidade não estiver habilitada, retorna uma lista vazia
    if not is_enabled:
        return []

    spoken_alerts = []  # Lista para armazenar as palavras que serão "faladas"

    # Itera sobre cada alerta da lista
    for alert in alerts:
        word = ""  # Variável para formar cada palavra
        count_letter = 0  # Contador de letras para detectar o fim do alerta

        # Itera sobre cada letra do alerta
        for letter in alert:
            count_letter += 1

            # Adiciona a letra à palavra se não for espaço
            if letter != " ":
                word += letter

            # Se encontrar espaço ou for a última letra do alerta, adiciona a palavra formada à lista
            if letter == " " or count_letter == len(alert):
                spoken_alerts.append(word)
                word = ""  # Reinicia a variável para formar a próxima palavra

    return spoken_alerts  # Retorna a lista com todas as palavras dos alertas


# Função principal para testar a funcionalidade
def main():
    alerts = ["Alerta de enchente", "Chuva forte", "Alerta de granizo"]  # Lista de alertas
    accessibility_enabled = True  # Acessibilidade ativada (simula leitor de tela)

    results = speak_alerts(alerts, accessibility_enabled)  # Processa os alertas

    print(results)  # Exibe as palavras que seriam "faladas"


# Ponto de entrada do script
if __name__ == "__main__":
    main()
