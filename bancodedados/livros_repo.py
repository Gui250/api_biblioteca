from bancodedados.conexao import cursor

def listar_todos():
    result = cursor.execute('select * from livros')
    livros = result.fetchall()
    lista = []
    for livro in livros: 
        lista.append({
            'id': livro[0], 
            'titulo': livro[1],
            'editora': livro[2],
            'ano': livro[3], 
            'autor': livro[4]
        })

    return lista

print(listar_todos())