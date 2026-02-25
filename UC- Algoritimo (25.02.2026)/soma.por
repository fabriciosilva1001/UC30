programa
{
	funcao inicio()
	{
		inteiro numero, soma, i
		soma = 0

		escreva("Digite um número: ")
		leia(numero)

		para (i = 1; i <= numero; i++)
		{
			soma = soma + i
		}

		escreva("Resultado: ", soma)
	}
}