def speak_alerts(alerts: list[str], is_enabled: bool) -> list[str]:
    if not is_enabled:
        return []

    spoken_alerts = []

    for alert in alerts:
        word = ""
        count_letter = 0

        for letter in alert:
            count_letter += 1

            if letter != " ":
                word += letter

            if letter == " " or count_letter == len(alert):
                spoken_alerts.append(word)
                word = ""

    return spoken_alerts


def main():
    alerts = ["Alerta de enchente", "Chuva forte", "Alerta de granizo"]
    accessibility_enabled = True

    results = speak_alerts(alerts, accessibility_enabled)

    print(results)


if __name__ == "__main__":
    main()
