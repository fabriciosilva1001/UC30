from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    dados = {
        'nome': request.args.get('nome'),
        'curso': request.args.get('curso'),
        'cidade': request.args.get('cidade'),
        'email': request.args.get('email')
    }
    return render_template('resultado.html', **dados)

if __name__ == '__main__':
    app.run(debug=True)