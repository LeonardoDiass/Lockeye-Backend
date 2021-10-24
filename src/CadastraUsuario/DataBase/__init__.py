import psycopg2

class DataBase():
    def __init__(self, DATABASE):
        self.conn = self.conexao(DATABASE)

    def conexao(self, DATABASE):
        try:
            return psycopg2.connect(dbname=DATABASE['dbname'], user=DATABASE['user'], host=DATABASE['host'], password=DATABASE['password'])
        except Exception as Erro:
            raise ("DATABASE ERRO: ",Erro)

    def select(self, sql):
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            cur.close()
            return row
        except Exception as Erro:
            raise ("SELECT ERRO: ",Erro)

    def update(self, sql):
        try: 
            cur = self.con.cursor()
            cur.execute(sql)
            self.con.commit()
            cur.close()
            return "SUCESSO"
        except Exception as Erro:
            return "UPDATE ERRO: ", Erro

    def insert(self, sql):
        try: 
            cur = self.con.cursor()
            cur.execute(sql)
            self.con.commit()
            cur.close()
            return "SUCESSO"
        except Exception as Erro:
            return "UPDATE ERRO: ", Erro
        


    