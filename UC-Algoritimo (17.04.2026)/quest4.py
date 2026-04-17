def academia():
    try:
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))

        imc = peso / (altura * altura)

        print("IMC:", imc)

        if imc < 18.5:
            print("Magro")
        elif imc <= 24.9:
            print("Normal")
        else:
            print("Sobrepeso")
            
    except:
        print("Entrada inválida! Use apenas números.")

academia()
