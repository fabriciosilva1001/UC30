def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


# Dicionário que liga opções às funções
operacoes = {
    "1": ("Soma", somar),
    "2": ("Subtração", subtrair),
    "3": ("Multiplicação", multiplicar),
    "4": ("Divisão", dividir)
}


while True:
    print("\n=== CALCULADORA DIFERENTE 😎 ===")
    
    for chave, valor in operacoes.items():
        print(f"{chave} - {valor[0]}")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Encerrando... 👋")
        break

    if escolha not in operacoes:
        print("Opção inválida! Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Use apenas números.")
        continue

    nome, funcao = operacoes[escolha]
    resultado = funcao(num1, num2)

    print(f"Resultado da {nome}: {resultado}")