import sqlite3
conexao = sqlite3.connect('cliente.db')
cursor = conexao.cursor()
p_nome = 'André'
p_idade = 46
sql = """
INSERT INTO clientes (nome, idade)
VALUES (?, ?)
"""
cursor.execute(sql, (p_nome, p_idade))
conexao.commit()
conexao.close()