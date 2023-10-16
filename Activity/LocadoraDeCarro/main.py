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

# codigo para executar no sql

# select *  from usuario;
# select *  from veiculo;


# create database locadora_brum;

# use locadora_brum;

# create table usuario(
# 	nome varchar(255),
#     cpf varchar(11),
#     telefone varchar(11),
#     nasc varchar(20),
#     senha varchar(255),
#     pais varchar(100),
#     cidade varchar(255),
#     estado varchar(255)
# );
 
# create table veiculo(
#   marca varchar(255),
#   modelo varchar(11),
#   cor varchar(11),
#   valor_diario varchar(20),
#   valor_mensal varchar(255),
#   valor_compra varchar(100)
# );

#==================================================================================================================

#importando metodos da conexao
# from Crud.Conexao import BancoPostgreSQL # para importar uma classe de outro arquivo

from Crud.Banco import *
#importa 
#from pasta1 import arquivo1

import pymysql.connections

#importando as Bibliotecas que seram usadas
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from arquivo import Ui_MainWindow
import sqlite3
import pymysql
import sys
import pandas as pd

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
        self.bnt_cadastrarVeiculoo.clicked.connect(self.cad_veiculo)
        # self.bnt_deletarUsuario.clicked.connect(self.deletarUser)

        # self.tabelaListaDeUsuarios.setCollumnWidth(self.tabelaListaDeUsuarios)

    #Funcao para cadastrar o usuario
    def inserirUsuario(self): 
        nome = self.txt_nome.text()
        cpf = self.txt_cpf.text()
        tel = self.txt_telefone.text()
        nasc = self.txt_dataNasc.text()
        senha = self.txt_senha.text()
        pais = self.txt_pais.text()
        cidade = self.txt_cidade.text()
        estado = self.txt_estado.text()
        classeBanco = Banco()
       
        sql = f"INSERT INTO usuario(nome,cpf,telefone,nasc,senha,pais,cidade,estado) VALUES('{nome}','{cpf}','{tel}','{nasc}','{senha}','{pais}','{cidade}','{estado}')"
        response = classeBanco.execute_query(sql)
        print(sql)
    
    #Funcao para cadastrar o veiculo
    def cad_veiculo(self):
    
        valorCompra = self.txt_valorCompra.text()
        diario = self.txt_valorDiario.text()
        mod = self.txt_modelo.text()
        mensal = self.txt_valorMensal.text()
        cor = self.txt_cor.text()
        marca = self.txt_marca.text()                                                          
        classeBanco = Banco()

        sql = f"INSERT INTO veiculo(marca, modelo,cor,valor_diario,valor_mensal,valor_compra) VALUES('{marca}','{mod}','{cor}','{diario}','{mensal}','{valorCompra}')"
        response = classeBanco.execute_query(sql)
        print(sql)

        deletarUsuario = self.bnt_deletarUsuario.text()                                                       
        classeBanco = Banco()

        sql = f"DELETE FROM usuario WHERE nome = '{deletarUsuario}'"
        response = classeBanco.execute_query(sql)
        print(sql)

    #Funcao para tabelaListaDeUsuarios
    # def tabelaListaDeUsuarios(self):
    #     # Suponha que você já tenha obtido os dados de carros e os armazenado em uma lista chamada 'dados'

    #     # Configura o número de linhas e colunas na tabela
    #     self.listaCarros.lista_carros.setRowCount(len(0,400))
    #     self.listaCarros.lista_carros.setColumnCount(9)

    #     # Conecta os botões aos slots
    #     self.listaCarros.novo_carro.clicked.connect(self.to_novo_carro)
    #     self.listaCarros.cad_user.clicked.connect(self.to_cadastrar_usuario)
    #     self.listaCarros.btn_sair.clicked.connect(self.sair)

    #     # Define os nomes das colunas
    #     nomes_colunas = ["ID", "NOME", "MODELO", "STATUS", "COR", "PRECO", "CATEGORIA", "", ""]
    #     self.listaCarros.lista_carros.setHorizontalHeaderLabels(nomes_colunas)

    #     # Aplica estilos à tabela
    #     self.listaCarros.lista_carros.setStyleSheet("QTableView::item:selected { color:#0f0; background:#000000; font-weight:900; }"
    #                                             "QTableCornerButton::section { background-color:#232326; }" 
    #                                             "QHeaderView::section { color:#fff; background-color:#232326; }"
    #                                             "QTableView::item { color:#fff }")

    #     # Preenche a tabela com os dados dos carros e adiciona botões "Editar" e "Excluir"
    #     for linha in range(0, len(veiculo)):
    #         for coluna in range(0, 7):
    #             self.listaCarros.lista_carros.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados[linha][coluna])))
    #             if coluna == 6:
    #                 btn_editar = QtWidgets.QPushButton("Editar")
    #                 btn_editar.clicked.connect(lambda state, linha=linha: self.to_editar_carro(dados[linha][0]))
    #                 btn_editar.setStyleSheet("color: #fff; background-color: #045033")
    #                 self.listaCarros.lista_carros.setCellWidget(linha, coluna + 1, btn_editar)
                    
    #                 if obCarro.carro_v_a(dados[linha][0]) == False:
    #                     btn_excluir = QtWidgets.QPushButton("Excluir")
    #                     btn_excluir.clicked.connect(lambda state, linha=linha: self.excluir_carro(dados[linha][0]))
    #                     btn_excluir.setStyleSheet("color: #fff; background-color: #670503")
    #                     self.listaCarros.lista_carros.setCellWidget(linha, coluna + 2, btn_excluir)


    

    #==================================================================================================================
    # Não Funcionou
    # Algum dia pode ser que de pra usar

    # def cadastrarUser(self):
    #     # if self.txt_senha.text() != self.

    #     nome = self.txt_nome.text()
    #     cpf = self.txt_cpf.text()
    #     telefone = self.txt_telefone.text()
    #     data_Nasc = self.txt_dataNasc.text()
    #     senha_Acess = self.txt_senha.text()
    #     pais = self.txt_pais.text()
    #     cidade = self.txt_cidade.text()
    #     estado = self.txt_estado.text()

    #     db = telaPrincipal()
    #     db.conexao_banco.Conexao()
    #     db.inserirUsuario(nome,cpf,telefone,data_Nasc,senha_Acess,pais,cidade,estado)
    #     db.sairconexao_banco()

    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.information)
    #     msg.setWindowTitle("Cadastro De Usuario")
    #     msg.setText("Cadastro Realizado com Sucesso!")
    #     msg.exec()

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
    #==================================================================================================================

# Iniciando a Tela Principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()