def soma_segura(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Entrada inválida")
        return 0
    else:
        return resultado