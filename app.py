from flask import Flask
from controladores import autores, livros

app = Flask(__name__)

app.add_url_rule('/autor', methods=['GET'] ,view_func=autores.autores)
app.add_url_rule('/autor', methods=['POST'], view_func=autores.cadastro)
app.add_url_rule('/autor/<int:id>', methods=['GET'], view_func=autores.buscar_autor)
app.add_url_rule('/autor/<int:id>', methods=['PUT'], view_func=autores.editar_autor)
app.add_url_rule('/autor/<int:id>', methods=['DELETE'], view_func=autores.excluir_autor)
app.add_url_rule('/livro', methods=['GET'], view_func=livros.livros)
app.add_url_rule('/livro', methods=['POST'], endpoint='cadastro_livro' ,view_func=livros.cadastrar_livro)
app.add_url_rule('/livro/<int:id>', view_func=livros.buscar_livro)
app.add_url_rule('/livro/<int:id>', methods=['PUT'], view_func=livros.editar_livro)
app.add_url_rule('/livro/<int:id>', methods=['DELETE'], view_func=livros.excluir_livro)
app.run(debug=True)