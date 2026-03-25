def resumo_notas(notas):
    if not notas:
        return None
    
    soma = 0
    maior = notas[0]
    menor = notas[0]
    
    for nota in notas:
        soma += nota
        
        if nota > maior:
            maior = nota
        
        if nota < menor:
            menor = nota
    
    media = soma / len(notas)
    
    return {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }


# Exemplo
notas = [7.5, 8.0, 6.5, 9.0, 10.0]
print(resumo_notas(notas))