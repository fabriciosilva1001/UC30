aluno = {}

aluno['nome'] = input("Nome do aluno: ")
aluno['nota1'] = float(input("Nota da prova 1: "))
aluno['nota2'] = float(input("Nota da prova 2: "))

aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2

print("\n--- Dados do Aluno ---")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

if aluno['media'] >= 7:
    situacao = "Aprovado"
elif aluno['media'] >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Situação: {situacao}")