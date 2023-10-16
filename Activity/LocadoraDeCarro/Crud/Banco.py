#conectando com o banco
import pymysql.connections
class Banco:
    def __init__(self) -> None:
        pass     
    def conectar(self):
        self.banco = pymysql.connections.Connection(host="localhost",
                                       user="root",
                                       passwd="",
                                       database="locadora_brum")
        
    def close_connection(self):
        self.banco = ""
        
    def execute_query(self,query):
        try:
            
            self.conectar()
            
            cursor = self.banco.cursor()
            cursor.execute(query)
            dados = cursor.fetchall()
            
            self.banco.commit()
            self.close_connection()
              
            return dados
        
        except Exception as erro:
            return erro

     