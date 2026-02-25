programa {
    funcao inicio() {
        inteiro n, i, soma
        
        escreva("Digite o valor de n: ")
        leia(n)

        i = 1
        soma = 0

        enquanto (i <= n) {
            soma = soma + i
            i = i + 1
        }

        escreva("A soma de 1 até ", n, " é: ", soma)
    }
}