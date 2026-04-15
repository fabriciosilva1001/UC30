def media_notas():
    contador = 0
    soma = 0

    while contador < 3:
        entrada = input(f"Informe a nota {contador + 1}: ")

        try:
            numero = float(entrada)
        except ValueError:
            print("Notas inválidas! Use apenas números.")
            return

        soma += numero
        contador += 1

    resultado = soma / 3
    print("Média =", format(resultado, ".2f"))