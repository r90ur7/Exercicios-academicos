import sqlite3
conexao = sqlite3.connect('cliente.db')
cursor = conexao.cursor()
a_nome = [ 'UGB', 'André',]
a_id = [1, 2]
for i in a_id:
 sql = """
 update clientes
 set nome = ?
 where id = ?
 """
 cursor.execute(sql, (a_nome[i-1], i))
conexao.commit()
conexao.close()
