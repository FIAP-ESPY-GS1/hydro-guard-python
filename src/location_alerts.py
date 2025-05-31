
def check_flood_alert(risk_coordinates: list[float], user_coord: float) -> str:
    for risk_coord in risk_coordinates:
        if risk_coord - 10 <= user_coord <= risk_coord + 10:
            return "🔴 Perigo iminente de enchente! Evacue imediatamente."

        if risk_coord - 30 <= user_coord <= risk_coord + 30:
            return "🟡 Área próxima a zona de risco de enchente. Fique em alerta."

    return "🟢 Você está em uma área segura. Nenhum risco próximo detectado."


def main():
    risk_coordinates = [-105.8, -23.5, -35.4, -23.4, 50.1, 120.5, 65.2, -30]

    user_coord = float(input("Digite coordenada do usuário: "))

    result = check_flood_alert(risk_coordinates, user_coord)

    print(result)


if __name__ == "__main__":
    main()
