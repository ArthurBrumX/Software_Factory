import psycopg2

class BancoPostgreSQL:
    def _init_(self, host, database, nome, password):
        self.host = host
        self.database = database
        # self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.nome = self.txt_nome.text()
        cpf = self.txt_cpf.text()
        telefone = self.txt_telefone.text()
        data_Nasc = self.txt_dataNasc.text()
        senha_Acess = self.txt_senha.text()
        pais = self.txt_pais.text()
        cidade = self.txt_cidade.text()
        estado = self.txt_estado.text()

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida ao PostgreSQL")
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")

    def desconectar(self):
        if self.connection is not None:
            self.cursor.close()
            self.connection.close()
            print("Conexão fechada com o PostgreSQL")

    def executar_query(self, query):
        if self.connection is not None:
            try:
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except psycopg2.Error as e:
                print(f"Erro ao executar a consulta: {e}")
                return None
        else:
            print("Conexão com o PostgreSQL não está aberta.")
            return None

# Exemplo de uso
if __name__ == "_main_":
    banco = BancoPostgreSQL(
        host="localhost",
        database="LocadoraDeCarros",
        user="postgres",
        password="12345"
    )
    banco.conectar()

    # Exemplo de consulta
    resultado = banco.executar_query("SELECT * FROM sua_tabela;")
    if resultado:
        for linha in resultado:
            print(linha)

    banco.desconectar()


# import psycopg2
# import pymysql.connections
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

# class BancoDeDados():

#     # Conectando com o bacno
#     def conexao_banco(self):
#         self.conexao = psycopg2.connect(
#             host = 'localhost',
#             user = 'postgres',
#             password = '12345',
#             database = 'LocadoraDeCarros',
#             port = '5432'
#         )

#         # print(self.conexao.info)
#         # print(self.conexao.status)
#         self.cursor = self.conexao.cursor()

# # Iniciando a classe
# if __name__ == "__main__":
#     db = BancoDeDados()
#     db.conexao_banco()
#     db.inserirUsuario()
    # db.criarTabelaUsuario()
    # db.criarTabelaVeiculos()

# ====================================================================


# crud

# cursor.close()
# self.conexao.close()

# Desconectando do banco

# def sairconexao_banco(self):
#     try:
#         self.conexao.close()

#     except:
#         pass

# Criando a Tabela Usuario    

# def criarTabelaUsuario(self):
#     try:
#         cursor = self.conexao.cursor()
#         cursor.execute("""
#             create table usuarios(
#             id_usuario serial primary key,
#             nome varchar(100) not null,
#             cpf float(11) not null,
#             telefone varchar(11) not null,
#             data_Nasc date,
#             senha_Acess varchar(150) not null,
#             pais varchar(100),
#             cidade varchar(100),
#             estado varchar(100)
#             );
#         """)

#     except AttributeError:
#         print("Faça a Conexao!")

# # Criando a Tabela Veiculo

# def criarTabelaVeiculos(self):
#     try:
#         cursor = self.conexao.cursor()
#         cursor.execute("""
#             create table veiculo(
#             id_veiculo serial primary key,
#             marca varchar(100) not null,
#             modelo varchar(100) not null,
#             cor varchar(100) not null,
#             valor_diario float(50) not null,
#             valor_mensal float(50) not null,
#             valor_compra float(50) not null
#             );
#         """)

#     except AttributeError:
#         print("Faça a Conexao!")