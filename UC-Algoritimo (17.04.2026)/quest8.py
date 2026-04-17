valor = float(input("Digite o valor da compra: "))

if valor > 500:
    total = valor * 0.80
elif valor >= 200:
    total = valor * 0.90
else:
    total = valor

print("Preço final: R$")
print(total)
