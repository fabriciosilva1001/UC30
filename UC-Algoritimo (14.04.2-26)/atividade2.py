def divisao(x, y):
    try:
        return (lambda a, b: a / b)(x, y)
    except ZeroDivisionError:
        return "Não divida por zero!"