# Importando o banco de dados .connections
import pymysql.connections

class Banco: #Criando uma classe banco que sera a conexao com o banco

    # TODA CLASSE TEM Q TER A FUNCAO __INIT__
    def __init__(self) -> None:
        pass

    # criando uma funcao com os dados do banco
    def conectar(self): # A funcao conectar vai receber os dados do banco
        self.banco = pymysql.connections.Connection(host ="localhost",
                                                    user="root",
                                                    password="",
                                                    database="locadoraDeCarros")
    
    # A funcao close fecha a conexao com o banco
    def close_connection(self):
        self.banco = ""


    # Funcao para executar o Query
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