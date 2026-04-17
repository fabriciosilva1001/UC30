vendas = [10, 15, 20, 25, 30, 35, 40]
soma = 0

for numero in vendas:
    if numero % 2 == 0:
        soma = soma + numero

print("Resultado da soma dos pares:")
print(soma)
