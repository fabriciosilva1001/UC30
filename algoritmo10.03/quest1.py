salario_base = 3500.00
bonus = 800.00
desconto = 250.00

salario_bruto = salario_base + bonus
salario_liquido = salario_bruto - desconto

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"Salário Líquido: R$ {salario_liquido}")
print(f"Tipo salario_base: {type(salario_base)}")
print(f"Tipo bonus: {type(bonus)}")
print(f"Tipo desconto: {type(desconto)}")
print(f"Tipo salario_bruto: {type(salario_bruto)}")
print(f"Tipo salario_liquido: {type(salario_liquido)}")