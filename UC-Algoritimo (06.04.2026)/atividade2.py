def analisar():
    lista = [int(input(f"Valor {i+1}: ")) for i in range(8)]

    vistos = set()
    repetidos = {}

    for item in lista:
        if item in vistos:
            repetidos[item] = repetidos.get(item, 1) + 1
        else:
            vistos.add(item)

    if repetidos:
        print("Repetições encontradas:")
        for k, v in repetidos.items():
            print(f"{k} apareceu {v} vezes")
    else:
        print("Sem números repetidos")

analisar()