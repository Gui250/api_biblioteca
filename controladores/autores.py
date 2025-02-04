from flask import make_response, jsonify, request
from bancodedados import autores_repo, livros_repo
def autores():
    autores = autores_repo.listar_todos()
    return make_response(jsonify(autores))


def cadastro():
    body = request.get_json()
    autor = autores_repo.cadastrar_autor(body['nome'])
    return make_response(jsonify(autor), 201)


def buscar_autor(id): 
    autor = autores_repo.buscar_autor(id)

    if autor == None: 
        return make_response({'message': 'Autor não encontrado'}, 404)
    
    return make_response(jsonify(autor))


def editar_autor(id):
    body = request.get_json()
    autor = autores_repo.buscar_autor(id)

    if autor == None: 
        return make_response({'mesage': "Autor não encontrado"}, 404)

    autores_repo.editar_autores(id, body['nome'])
    return make_response({}, 204)

def excluir_autor(id):
    autor = autores_repo.buscar_autor(id)

    if autor == None: 
        return make_response({'message': 'Autor não encontrado'})
    
    livros = livros_repo.buscar_autor_livro(id)
    if len(livros) > 0:
        return make_response({'message': 'Autor não pode ser excluido pois contem livros'}, 400)


    autores_repo.excluir_autor(id)
    return make_response({}, 204)