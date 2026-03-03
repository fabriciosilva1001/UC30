n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(n1 + n2)
print(n1 * n2)

n = int(input("Digite um número inteiro: "))
if n % 2 == 0:
    print(n * n)
else:
    print(n * n * n)

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
if (usuario == "procopio" and senha == "12345") or (usuario == "paiva" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")

tentativas = 3
while tentativas > 0:
    acesso = input("Digite a senha do banco: ")
    if acesso == "123456":
        print("Olá, SEUNOME. Seja bem-vindo ao nosso banco!")
        tentativas = 0
    else:
        tentativas = tentativas - 1
        if tentativas == 2:
            print("Senha incorreta! Você ainda tem 2 tentativas.")
        elif tentativas == 1:
            print("Senha incorreta! Você ainda tem 1 tentativa.")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")