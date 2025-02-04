from flask import make_response, jsonify, request
from bancodedados import livros_repo, autores_repo

def livros():
    livros = livros_repo.listar_todos()
    return make_response(jsonify(livros))

def cadastrar_livro():
    body = request.get_json()
    autor = autores_repo.buscar_autor(body['autor_id'])

    if autor == None:
        return make_response({'message': 'Autor não encontrado'}, 404)

    livro = livros_repo.cadastrar_livro(body['titulo'], body['editora'], body['ano'], body['autor_id'])
    return make_response(jsonify(livro), 201)