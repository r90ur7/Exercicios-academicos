class MyCrud:
    
    
    def __init__(self,banco):
        import sqlite3 
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()
        
    def fecharmoleza(self):
        self.conexao.close()
        print('fim da operação.')
        
    def criarmoleza(self):
        sql = """
        CREATE TABLE IF NOT EXISTS PESSOAS(
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf INTEGER
        );
     """
        self.cursor.execute(sql)
        print('tabela criada')
    
    def selecionar(self):        
        sql =''' 
            SELECT * FROM PESSOAS;
        '''
        resultado = self.cursor.execute(sql)
        return resultado.fetchall()
    
        
    def inserir(self,id,nome,cpf):
        sql = """
          INSERT INTO PESSOAS(id,nome,cpf)
          VALUES(?,?,?)     
        """
        self.cursor.execute(sql,(id,nome,cpf))
        self.conexao.commit()
        print('salvo com sucesso...')
          
    def alterar(self, id, nome, cpf):
        sql = '''
            update PESSOAS
            set nome = ?, cpf = ?
            where id = ?;
        '''
        self.cursor.execute(sql, [nome, cpf, id])
        self.conexao.commit()
        print('alterado com sucesso...')
        
    def deletar(self,id):
        sql ='''
            DELETE FROM PESSOAS
            WHERE id = ?;
        '''
        self.cursor.execute(sql,(id,))
        self.conexao.commit()
        print('deletado com sucesso...')
        
        
        
        
        
        
        
        
        