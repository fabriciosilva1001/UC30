def calcular_total():
    valores = []
    indice = 1

    while indice <= 2:
        entrada = input(f"Preço do produto {indice}: ")

        try:
            valor = float(entrada)
        except ValueError:
            print("Preço inválido! Digite apenas números.")
            return

        valores.append(valor)
        indice += 1

    total = 0
    for v in valores:
        total += v

    print("Valor total da compra: R$", format(total, ".2f"))