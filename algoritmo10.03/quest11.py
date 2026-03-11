soma_pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma_pares += i

print(f"A soma dos números pares de 1 a 100 é: {soma_pares}")