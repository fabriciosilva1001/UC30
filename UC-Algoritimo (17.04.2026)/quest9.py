notas_turma = [8.5, 5.0, 7.5, 6.0, 9.0, 4.0, 10.0]
notas_boas = []

for nota in notas_turma:
    if nota > 7:
        notas_boas.append(nota)

print("Total de notas acima de 7:")
print(len(notas_boas))
