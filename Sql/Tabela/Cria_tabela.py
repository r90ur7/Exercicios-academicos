import sqlite3

conexao = sqlite3.connect('cliente2.db')
cursor = conexao.cursor()

sql = """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
    );
"""

cursor.execute(sql)

print('tabela criada...')


conexao.close()