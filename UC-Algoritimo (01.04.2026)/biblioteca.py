# Dicionario para armazemar os livros:
catalogo = []

# Dicionario para armazenar os emprestimos:
emprestimosativo = {}
# Lista para armazenar o historico de transição:
historico = []

def adicionarlivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"erro: livro com codigo {codigo} já existe!")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"livro '{titulo}' adicionado com sucesso")
    return True
#---------------------------------------------------------------------------------------------------------------------------
def livro_mais_popular():
    contagem = {}

    # O código a baixo, verifica os empréstimsos:
    for emprestimo in historico:
        codigo = emprestimo["codigo"]

        if codigo in contagem:
            contagem[codigo] += 1
        else:
            contagem[codigo] = 1

    # Agora o código vai checar se existe algum empréstimo presente:
    if not contagem:
        print("nenhum empréstimo registrado.")
        return None

    # Aqui o código após percorrer por todos os dados, vai retornar o livro mais popular:
    mais_popular = max(contagem, key=contagem.get)

    livro = catalogo.get(mais_popular)

    print("livro mais popular:")
    print(f"titulo: {livro['titulo']}")
    print(f"autor: {livro['autor']}")
    print(f"emprestimos: {contagem[mais_popular]}")
    return livro