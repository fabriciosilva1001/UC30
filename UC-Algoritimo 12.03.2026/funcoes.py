print("python é fácil")
print("python é fácil")
print("python é fácil")

def exibirmensagem():
    print("olá, mundo")

exibirmensagem()

def saudar(nome):
    print(f"olá, {nome} !")

saudar("Paulo")
saudar("Fabrício")

def exibirmensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

exibirmensagem("Paulo, bom dia")

exibirmensagem(nome = "Fabrício", mensagem = "boa noite")

def calcularmedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcularmedia(8.0, 9.0)
print(f"media: {resultado}")
    