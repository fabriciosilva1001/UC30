nome = input("Digite o nome completo do aluno: ")
matricula = int(input("Digite a matrícula: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("\n--- FICHA ESCOLAR ---")
print(f"ALUNO: {nome}")
print(f"MATRÍCULA: {matricula}")
print(f"NOTAS: {nota1} e {nota2}")
print(f"MÉDIA FINAL: {media}")
print("----------------------")