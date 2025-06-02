def get_safety_tip(region_name: str, regions: list[str], tips: list[str]):
  count = 0
  for i in regions:

      if i == region_name:
         return [tips[count]]
      count += 1

  return ["Região não encontrada."]



def main():
    regions = ["Zona Norte", "Zona Sul", "Centro"]
    tips = ["Evite áreas alagadas", "Mantenha-se em locais altos", "Use transporte público"]
    region_name = "Zona Sudeste"

    get_safety_tip(region_name, regions, tips)


if __name__ == "__main__":
    main()
