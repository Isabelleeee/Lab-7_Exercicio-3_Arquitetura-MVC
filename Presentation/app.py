from flask import Flask, render_template
from infrastructure.repository import LivroRepository
from services.livro_service import LivroService

app = Flask(__name__)

# Injeção de dependência simples
repo = LivroRepository()
service = LivroService(repo)

@app.route('/')
def index():
    # A UI só fala com o Service, nunca com o Repository diretamente!
    livros = service.obter_catalogo_disponivel()
    return render_template('index.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)