# O aluno deverá desenvolver uma aplicação em Python utilizando PyQt ou PySide, 
# para uma locadora de veículos, comunicando com o banco de dados no qual deverá ter as seguintes funcionalidades: 

# - Opções para locar o carro por diária 
# - Opções para locar o carro mensalista 
# - Opções de compra do carro 

# Categorias (aluguel-diario, compra, Mensalista)

# O sistema deverá permitir cadastrar os veículos e em qual categoria ele se enquadra. 
# (Cadastrar, R(mostrar os dados), U(editar os dados), D(deletar se o carro nunca foi alugado ou vendido)). 
# Cadastrar usuário para realizar a venda ou a locação. 
#==================================================================================================================

#importando metodos da conexao
from Crud.Conexao import BancoPostgreSQL # para importar uma classe de outro arquivo

# importa 
#from pasta1 import arquivo1

import pymysql.connections

#importando as Bibliotecas que seram usadas
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from arquivo import Ui_MainWindow
import sqlite3
import pymysql
import psycopg2
import sys

# Testando sem a importacao aq

    # Criando um instaciamento (chamando o banco)
    # db = BancoDeDados()
    # db.conexao_banco.Conexao()

# Criando a classe das Telas
class telaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(telaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Principal")

        # Conectando os Botoes (menu)
        self.bnt_home.clicked.connect(lambda: self.janelaDeNavegacao.setCurrentWidget(self.home))
        self.bnt_cadastrarUser.clicked.connect(lambda: self.janelaDeNavegacao.setCurrentWidget(self.page_cadastrarUser))
        self.bnt_cadastrarVeiculo.clicked.connect(lambda: self.janelaDeNavegacao.setCurrentWidget(self.page_cadastrarVeiculo))
        self.bnt_listaUser.clicked.connect(lambda: self.janelaDeNavegacao.setCurrentWidget(self.page_listaDeUsuarios))
        self.bnt_listaVeiculo.clicked.connect(lambda: self.janelaDeNavegacao.setCurrentWidget(self.page_listaDeVeiculos))
        # Final das Conecoes com as telas (menu)

        self.bnt_cadastrarUsuario.clicked.connect(self.inserirUsuario)


    def inserirUsuario(self):
        self.bnt_cadastrarUsuario.clicked.connect(self.inserirUsuario)

    def cadastrarUser(self):
        # if self.txt_senha.text() != self.

        nome = self.txt_nome.text()
        cpf = self.txt_cpf.text()
        telefone = self.txt_telefone.text()
        data_Nasc = self.txt_dataNasc.text()
        senha_Acess = self.txt_senha.text()
        pais = self.txt_pais.text()
        cidade = self.txt_cidade.text()
        estado = self.txt_estado.text()

        db = BancoPostgreSQL()
        db.conexao_banco.Conexao()
        db.inserirUsuario(nome,cpf,telefone,data_Nasc,senha_Acess,pais,cidade,estado)
        db.sairconexao_banco()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.information)
        msg.setWindowTitle("Cadastro De Usuario")
        msg.setText("Cadastro Realizado com Sucesso!")
        msg.exec()


    # def inserirUsuario(self):
    #     self.bnt_cadastrarUsuario.clicked.connect(self.inserirUsuario)
    #     try:
    #         cursor = self.conexao.cursor()
    #         cursor.execute("""
    #             INSERT INTO usuarios(cpf,telefone,data_Nasc,senha_Acess,pais,cidade,estado) VALUES(%s,%s,%s,%s,%s,%s,%s)
    #         """,(self.nome,self.cpf,self.telefone,self.dataNascimento,self.senha_Acess,self.pais,self.cidade,self.estado))

    #         self.conexao.commit() 
    #         print("Usuario Adcionado!")   

    #     except AttributeError:
    #         print("Faça a Conexao!")

# Iniciando a Tela Principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()