from flask import make_response, jsonify, request
from bancodedados import autores_repo

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