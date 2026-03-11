senha = input("Digite a senha: ")

total_numeros = 0

for caractere in senha:
    if caractere.isdigit():
        total_numeros += 1

if len(senha) >= 8 and total_numeros > 0:
    print("Senha válida")
else:
    print("Senha inválida")