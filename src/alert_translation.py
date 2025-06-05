from enum import Enum


# Enum para representar os tipos de alerta disponíveis
class AlertType(Enum):
    ENCHENTE = "enchente"
    CHUVA = "chuva"
    DESLIZAMENTO = "deslizamento"


# Função que retorna a mensagem de alerta traduzida com base na opção e tipo de alerta
def get_alert_message(option: int, alert_type: AlertType) -> str:
    # Listas com mensagens em 3 idiomas: [Português, Inglês, Espanhol]
    floods = ["Alerta de enchente", "Flood alert", "Alerta de inundación"]
    rains = ["Alerta de chuva", "Heavy rain expected", "Alerta de lluvia intensa"]
    landslides = ["Alerta de deslize", "Landslide warning", "Alerta de deslizamiento"]

    # Validação: se a opção for inválida, retorna mensagem de erro
    if option < 0 or option > 2:
        return "Opção inválida."

    # Seleciona a mensagem correta com base no tipo de alerta
    if alert_type == AlertType.ENCHENTE:
        return floods[option]
    elif alert_type == AlertType.CHUVA:
        return rains[option]
    elif alert_type == AlertType.DESLIZAMENTO:
        return landslides[option]


# Função principal que coleta entrada do usuário e imprime a mensagem correspondente
def main():
    # Solicita a opção de idioma
    option = int(input("Escolha uma opção de tradução (0 - Português, 1 - Inglês, 2 - Espanhol): "))

    # Solicita o tipo de alerta e converte para Enum
    alert_type = AlertType(input("Digite o tipo de alerta (enchente, chuva, deslizamento): "))

    # Obtém a mensagem traduzida
    message = get_alert_message(option, alert_type)

    # Exibe a mensagem final
    print(message)


# Executa o programa se for executado diretamente
if __name__ == "__main__":
    main()
