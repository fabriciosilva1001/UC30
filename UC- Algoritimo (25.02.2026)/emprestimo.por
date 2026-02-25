programa
{
	funcao inicio()
	{
		real casa, salario, prestacao
		inteiro anos

		escreva("Valor da casa: ")
		leia(casa)
		escreva("Seu salário: ")
		leia(salario)
		escreva("Quantos anos para pagar: ")
		leia(anos)
*-+	
		prestacao = casa / (anos * 12)

		se (prestacao > salario * 0.3)
		{
			escreva("Empréstimo Negado.")
		}
		senao
		{
			escreva("Empréstimo Aprovado!")
		}
	}
}