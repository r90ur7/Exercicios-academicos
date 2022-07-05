import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

sql = '''
DELETE FROM clientes
WHERE id = ?;
'''

p_id = 1

cursor.execute(sql, [p_id])
conexao.commit()
print('deletado com sucesso...')
conexao.close()