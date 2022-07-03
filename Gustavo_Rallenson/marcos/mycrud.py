class MyCrud:

    def __init__(self, banco):
        import sqlite3
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def criar_moleza(self):
        sql = '''
            create table if not exists individuos(
                id integer not null primary key autoincrement,
                nome text not null,
                cpf character(11) not null
            );
        '''
        self.cursor.execute(sql)
        print('Tabela criada...')

    def fechar_moleza(self):
        self.conexao.close()
        print('A operação foi encerrada!')

    def selecao(self):
        sql = '''
            select * from individuos;
        '''
        resultado = self.cursor.execute(sql)
        return resultado.fetchall()

    def colocar (self,id, nome,cpf):
        sql = '''
            insert into individuos(id,nome,cpf)
            values(?,?,?)
        '''
        self.cursor.execute(sql,(id,nome,cpf))
        self.conexao.commit()
        print('Dados salvos no banco de dados')

    def mudar(self, id, nome, cpf):
        sql = '''
            update individuos
            set nome = ?, cpf = ?
            where id = ?;
        '''
        self.cursor.execute(sql, [nome,cpf,id])
        self.conexao.commit()
        print('Dados alterados no banco de dados')

    def excluir(self,id,):
        sql = '''
            delete from individuos
            where id = ?;
        '''
        self.cursor.execute(sql,(id,))
        self.conexao.commit()
        print('Dado delatado do banco de dados')

