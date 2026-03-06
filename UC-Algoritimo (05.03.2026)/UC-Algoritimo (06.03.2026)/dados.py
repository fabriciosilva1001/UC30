# quadrados de 1 a 10
quadrados = [x**2 for x in range(1,11)]
print("Quadrado: ", quadrados)

# números pares de 1 a 20
pares = [x for x in range(1,21) if x % 2 == 0]
print("Pares: ", pares)

# vogais de programação
vogais = [letra for letra in "PROGRAMAÇÃO" if letra in "AEIOU"]
print("Vogais: ", vogais)