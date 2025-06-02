def find_safe_routes(distances: list[float] = list()) -> list[float]:
    aux = 0
    for i in range(0, len(distances)):
        for j in range(i+1, len(distances)):

            if distances[i] > distances[j]:

               aux = distances[i]
               distances[i] = distances[j]
               distances[j] = aux

    if len(distances) >= 3:
        return distances[0:3]
    else:
        return distances[0:len(distances)]


def main():
   distances = [10.6 ,20, 30.5, 2, 40, 50]
   result = find_safe_routes(distances)
   print(result)


if __name__ == "__main__":
    main()
