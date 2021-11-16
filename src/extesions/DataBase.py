import psycopg2

class DataBase():
    def __init__(self, CONFIG):
        self.conn = self.connection(CONFIG['DATABASE'])

    def connection(self, DATABASE):
        try:
            conn = psycopg2.connect(dbname=DATABASE['dbname'], user=DATABASE['user'], host=DATABASE['host'], password=DATABASE['password'])
            return conn
        except Exception as Erro:
            raise "ERRO BANCO DE DADOS: " + Erro

    def select(self, sqlstr):
        try:
            cur = self.conn.cursor()
            cur.execute(sqlstr)
            row = cur.fetchone()
            cur.close()
            return row
        except Exception as Erro:
            raise "SELECT ERRO: " + Erro

    def update(self, sqlstr):
        try: 
            cur = self.conn.cursor()
            cur.execute(sqlstr)
            self.conn.commit()
            cur.close()
        except Exception as Erro:
            raise "ERRO UPDATE: " + Erro

    def insert(self, sqlstr):
        try: 
            cur = self.conn.cursor()
            cur.execute(sqlstr)
            self.conn.commit()
            cur.close()
        except Exception as Erro:
            raise "ERRO UPDATE: " + Erro






   

