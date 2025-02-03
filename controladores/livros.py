from flask import make_response, jsonify
from bancodedados import livros_repo

def livros():
    livros = livros_repo.listar_todos()
    return make_response(jsonify(livros))