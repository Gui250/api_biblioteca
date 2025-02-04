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


def buscar_livro(id):
    livro = livros_repo.buscar_livro(id)

    if livro == None:
        return make_response({'message': 'Livro não encontrado'}, 404)
    
    return make_response(jsonify(livro))


def editar_livro(id):
    body = request.get_json()
    livro = livros_repo.buscar_livro(id)

    if livro == None: 
        return make_response({'mesage': "livro não encontrado"}, 404)
    
    autor = autores_repo.buscar_autor(body['autor_id'])
    if autor == None: 
        return make_response({'message': 'Autor não encontrado'}, 404)

    livros_repo.editar_livro(id, body['titulo'], body['editora'], body['ano'], body['autor_id'])
    return make_response({}, 204)

def excluir_livro(id):
    livro = livros_repo.buscar_livro(id)

    if livro == None: 
        return make_response({'message': 'Livro não encontrado'}, 404)
    
   
    livros_repo.excluir_livro(id)
    return make_response({}, 204)