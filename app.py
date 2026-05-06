from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = "centralia"

# ===== MODELO =====
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

# ===== DAO =====
class LivroDAO:
    def __init__(self):
        self.banco_de_dados = []

    def salvar(self, livro):
        self.banco_de_dados.append(livro)

    def listar(self):
        return self.banco_de_dados

dao = LivroDAO()

# ===== ROTAS =====
@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/novo_livro", methods=["POST"])
def novo_livro():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    paginas = request.form.get('paginas')

    try:
        paginas = int(paginas)

        if paginas <= 0:
            raise ValueError()

    except ValueError:
        flash("Número de páginas inválido! Use apenas números positivos.")
        return redirect(url_for("formulario"))

    livro = Livro(titulo, autor, paginas)
    dao.salvar(livro)

    return redirect(url_for("lista"))


@app.route("/lista")
def lista():
    livros = dao.listar()
    return render_template("lista.html", livros=livros)

if __name__ == "__main__":
    app.run(debug=True)