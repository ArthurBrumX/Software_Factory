# Deu tudo errado!
# Faz de novo!

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