from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def inicio():
    preferencias = {
        'nome': request.cookies.get('nome_usuario'),
        'tema': request.cookies.get('tema_usuario', 'claro')
    }
    return render_template('inicio.html', **preferencias)

@app.route('/configurar/<acao>', methods=['POST', 'GET'])
def configurar(acao):
    resposta = make_response(redirect(url_for('inicio')))
    um_mes = 60 * 60 * 24 * 30

    acoes = {
        'nome': lambda: resposta.set_cookie('nome_usuario', request.form.get('nome', ''), max_age=um_mes),
        'tema': lambda: resposta.set_cookie('tema_usuario', request.args.get('valor', 'claro'), max_age=um_mes),
        'limpar': lambda: [resposta.delete_cookie('nome_usuario'), resposta.delete_cookie('tema_usuario')]
    }

    if acao in acoes:
        acoes[acao]()

    return resposta

if __name__ == '__main__':
    app.run(debug=True)