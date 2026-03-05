import random

numeros = [91, 34, 67, 15, 82]

print("Lista original:", numeros)

numeros.sort()
print("Ordem crescente:", numeros)

numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)

numeros3 = [6, 7, 8, 9, 10]

random.shuffle(numeros3)
print("Lista embaralhada:", numeros3)

numeros4 = [14, 3, 29, 8, 17, 1]

print("Terceira lista original:", numeros4)

numeros4.sort()
print("Terceira crescente:", numeros4)

numeros4.sort(reverse=True)
print("Terceira decrescente:", numeros4)

random.shuffle(numeros4)
print("Terceira embaralhada:", numeros4)