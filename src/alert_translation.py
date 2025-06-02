from enum import Enum


class AlertType(Enum):
    ENCHENTE = "enchente"
    CHUVA = "chuva"
    DESLIZAMENTO = "deslizamento"


def get_alert_message(option: int, alert_type: AlertType) -> str:
    floods = ["Alerta de enchente", "Flood alert", "Alerta de inundación"]
    rains = ["Alerta de chuva", "Heavy rain expected", "Alerta de lluvia intensa"]
    landslides = ["Alerta de deslize", "Landslide warning", "Alerta de deslizamiento"]

    if option < 0 or option > 2:
        return "Opção inválida."

    if alert_type == AlertType.ENCHENTE:
        return floods[option]
    elif alert_type == AlertType.CHUVA:
        return rains[option]
    elif alert_type == AlertType.DESLIZAMENTO:
        return landslides[option]


def main():
    option = int(input("Escolha uma opção de tradução (0 - Português, 1 - Inglês, 2 - Espanhol): "))
    alert_type = AlertType(input("Digite o tipo de alerta (enchente, chuva, deslize): "))

    message = get_alert_message(option, alert_type)

    print(message)


if __name__ == "__main__":
    main()
