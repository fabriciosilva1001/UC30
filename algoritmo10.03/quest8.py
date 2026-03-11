valor_compra = float(input("Valor da compra: R$ "))

if valor_compra < 100:
    percentual = 0
elif valor_compra < 500:
    percentual = 5
elif valor_compra < 1000:
    percentual = 10
else:
    percentual = 15

desconto = valor_compra * (percentual / 100)
valor_final = valor_compra - desconto

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto ({percentual}%): R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")