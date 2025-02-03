from bancodedados.conexao import cursor, con
def listar_todos():
    result = cursor.execute('select * from autores')
    autores = result.fetchall()
    lista = []
    for autor in autores: 
        lista.append({
            'id': autor[0], 
            'nome': autor[1]
        })

    return lista

print(listar_todos())


def cadastrar_autor(nome):
    result = cursor.execute('insert into autores (nome) values (%s) returning *', (nome, ))
    con.commit()
    autor = result.fetchone()
    return {
        'id': autor[0],
        'nome': autor[1]
    }

def buscar_autor(id): 
    result = cursor.execute('select * from autores where id = %s', (id, ))
    autor = result.fetchone()
    
    if autor == None: 
        return None
    
    return {
        'id': autor[0],
        'nome': autor[1]
    }