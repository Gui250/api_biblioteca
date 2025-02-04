from bancodedados.conexao import cursor, con

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


def buscar_autor_livro(autor_id):
    result = cursor.execute('select * from livros where autor_id = %s', (autor_id, ))
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


def cadastrar_livro(titulo, editora, ano, autor_id):
    result = cursor.execute('insert into livros (titulo, editora, ano, autor_id) values (%s, %s, %s, %s) returning *', (titulo, editora, ano, autor_id ))
    con.commit()
    livro = result.fetchone()
    return {
        'id': livro[0],
        'titulo': livro[1],
        'editora': livro[2],
        'ano': livro[3],
        'autor': livro[4]
    }


def buscar_livro(id):
    result = cursor.execute('select * from livros where id = %s', (id, ))
    livro = result.fetchone()

    if livro == None: 
        return None 
    
    return {
        'id': livro[0],
        'titulo': livro[1], 
        'editora': livro[2],
        'ano': livro[3],
        'autor': livro[4]
    }


def editar_livro(id, titulo, editora, ano, autor_id):
    cursor.execute('update livros set titulo = %s, editora = %s, ano = %s, autor_id = %s where id = %s', (titulo, editora, ano, autor_id, id))
    con.commit()
    return True


def excluir_livro(id):
    cursor.execute('delete from livros where id = %s', (id, ))
    con.commit()
    return True