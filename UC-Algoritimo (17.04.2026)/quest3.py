total = 0
valor = -1

print("Calculadora do Supermercado")
print("Use ponto para centavos (ex: 10.50)")

while valor != 0:
    valor = float(input("Digite o valor do item: "))
    total = total + valor

print("O total da sua compra é: R$")
print(total)
