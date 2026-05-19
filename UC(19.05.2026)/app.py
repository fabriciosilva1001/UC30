from flask import Flask, render_template

app = Flask(__name__)

PRODUTOS = {
    "burguer-classico": {"nome": "Burguer Clássico", "preco": "R$ 19,90", "ingredientes": "Carne 150g, queijo e molho da casa."},
    "batata-frita": {"nome": "Batata Suprema", "preco": "R$ 14,50", "ingredientes": "Batatas crocantes com cheddar e bacon."},
    "refri-lata": {"nome": "Refrigerante Lata", "preco": "R$ 6,00", "ingredientes": "Lata de 350ml trincando de gelada."}
}

@app.route('/')
def pagina_home():
    return render_template('home.html')

@app.route('/menu')
def pagina_menu():
    return render_template('menu.html', cardapio=PRODUTOS)

@app.route('/item/<slug>')
def detalhe_item(slug):
    comida = PRODUTOS.get(slug)
    if comida:
        return render_template('detalhe.html', info=comida)
    return "Item não encontrado!", 404

@app.route('/meu-carrinho')
def pagina_sacola():
    return render_template('sacola.html')

@app.route('/fale-conosco')
def pagina_suporte():
    return render_template('suporte.html')

@app.route('/usuario/<username>')
def painel_usuario(username):
    return render_template('usuario.html', nome=username)

if __name__ == '__main__':
    app.run(debug=True)
