from flask import Flask
from controladores import autores, livros

app = Flask(__name__)

app.add_url_rule('/autor', methods=['GET'] ,view_func=autores.autores)
app.add_url_rule('/livro', methods=['GET'], view_func=livros.livros)
app.add_url_rule('/autor', methods=['POST'], view_func=autores.cadastro)
app.add_url_rule('/autor/<int:id>', methods=['GET'], view_func=autores.buscar_autor)
app.run(debug=True)