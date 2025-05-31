def get_safety_tip(region_name: str, regions: list[str], tips: list[str]):
    print(region_name)
    print(regions)
    print(tips)


def main():
    regions = ["Zona Norte", "Zona Sul", "Centro"]
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos", "Use transporte público"]
    region_name = "Zona Sul"

    get_safety_tip(region_name, regions, tips)


if __name__ == "__main__":
    main()
