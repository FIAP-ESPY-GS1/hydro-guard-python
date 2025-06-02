def check_risk_zones(user_path: list[float], risk_zones: list[float]) -> list[float]:
    cord_risks = []
    for i in user_path:
        for j in risk_zones:
            if i == j:
                cord_risks.append(i)

    return cord_risks


def main():
    user_path = [100, 300, 155, 124]
    risk_zones = [100, 150, 200, 300]

    result = check_risk_zones(user_path,risk_zones)

    print(result)


if __name__ == "__main__":
    main()
