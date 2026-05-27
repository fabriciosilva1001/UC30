from flask import Flask, render_template

site = Flask(__name__)

@site.route("/")
def menu():
    return render_template("index.html")

@site.route("/cursos")
def curso():
    return render_template("cursos.html")

@site.route("/professores")
def prof():
    return render_template("professores.html")

@site.route("/contato")
def falar():
    return render_template("contato.html")

if __name__ == "__main__":
    site.run(debug=True)