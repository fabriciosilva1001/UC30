texto = input("Escreve uma frase: ")
vogais = "aeiouAEIOU"
total_vogais = 0

for letra in texto:
    if letra in vogais:
        total_vogais = total_vogais + 1

print("Quantidade de vogais encontradas:")
print(total_vogais)
