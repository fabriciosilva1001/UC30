numeros = [80, 20, 30, 20, 40, 90, 50]

print("Lista:", numeros)

tamanho = len(numeros)
print("Total de elementos:", tamanho)

repeticoes = numeros.count(20)
print("O número 20 aparece:", repeticoes, "vezes")

posicao = numeros.index(30)
print("Posição do número 30:", posicao)

if 100 in numeros:
    print("O número 100 está na lista")
else:
    print("O número 100 não está na lista")