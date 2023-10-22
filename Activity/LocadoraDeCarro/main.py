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
# from Crud.Conexao import BancoPostgreSQL # para importar uma classe de outro arquivo

from Crud.Banco import *
#importa 
#from pasta1 import arquivo1

import pymysql.connections

#importando as Bibliotecas que seram usadas
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow,QStackedWidget,QLabel
import sqlite3
from telaMain import Ui_MainWindow
import pymysql
import sys


# Testando sem a importacao aq

    # Criando um instaciamento (chamando o banco)
    # db = BancoDeDados()
    # db.conexao_banco.Conexao()

#instanciamento do banco de dados
classeBanco = Banco()

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

        # Executando Fucnoes
        self.bnt_cadastrarUsuario.clicked.connect(self.inserirUsuario)
        self.bnt_cadastrarVeiculoo.clicked.connect(self.cad_veiculo)
        self.bnt_deletarUsuario.clicked.connect(self.deletar_usuario)
        self.btn_deletarVeiculo.clicked.connect(self.deletar_veiculo)
        self.bnt_listaUser.clicked.connect(self.listarUsuario)
        self.bnt_listaVeiculo.clicked.connect(self.listarVeiculo)
        self.btn_alugarDiaria.clicked.connect(self.alugarVeicDiaria)
        self.btn_alugarMensal.clicked.connect(self.alugarVeicMesal)
        self.btn_comprar.clicked.connect(self.comprarVeic)

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
        print("Usuario Cadastrado Com Sucesso!")
    
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
        print("Veiculo Cadastrado Com Sucecsso")

    # #Funcao para deletar Usuario
    def deletar_usuario(self):

        deletarUser = self.txt_DeletarIDUser.text()
        classeBanco = Banco()

        sql = f"DELETE FROM usuario WHERE id_usuario = {deletarUser}"
        response = classeBanco.execute_query(sql)
        print(sql)
        print("Usuario Deletado Com Sucesso!")

    # Funcao para deletar veiculo
    def deletar_veiculo(self):

        deletarVeic = self.txt_idVeiculo.text()
        classeBanco = Banco()

        sql = f"DELETE FROM veiculo WHERE id_veiculo = {deletarVeic}" # uma variavel que contem um comando sql
        response = classeBanco.execute_query(sql) # execute_query() - executa um comando sql
        print(sql)
        print("Veiculo Deletado Com Sucesso!")

    # Funcao para listar clientes
    def listarUsuario(self):
        # Mostrar os dados do banco de dados

        classeBanco = Banco()
        sql = "SELECT * FROM usuario"
        response = classeBanco.execute_query(sql)
        print(response)

        self.tabelaListaDeUsuarios.setRowCount(len(response))
        self.tabelaListaDeUsuarios.setColumnCount(9)

        for linha in range(0, len(response)):
            for coluna in range(0,9):
                self.tabelaListaDeUsuarios.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(response[linha][coluna])))

    # funcao Listar Veiculo
    def listarVeiculo(self):
        # Mostrar os dados do banco de dados

        classeBanco = Banco()
        sql = "SELECT * FROM veiculo"
        response = classeBanco.execute_query(sql)
        print(response)

        self.tabelaListaDeVeiculos.setRowCount(len(response))
        self.tabelaListaDeVeiculos.setColumnCount(7)

        for linha in range(0, len(response)):
            for coluna in range(0,7):
                self.tabelaListaDeVeiculos.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(response[linha][coluna])))

    #Funcao Alugar o carro diariamente
    def alugarVeicDiaria(self):
        alugaDi = self.txt_idVeiculo.text()
        classeBanco = Banco()

        # inserção dos dados na tabela de aluguel
        sql_insercao = f"INSERT INTO veiculoAlugadosDiaria (id_veiculo) SELECT {alugaDi} FROM veiculo WHERE id_veiculo = {alugaDi};"
        
        # selecionando os dados que acabou de ser inserido
        sql_selecao = f"SELECT {alugaDi} FROM veiculoAlugadosDiaria;"

        # excluir o veículo da tabela de veículos
        sql_exclusao = f"DELETE FROM veiculo WHERE id_veiculo = {alugaDi};"

        # Executando a consulta SQL
        response = classeBanco.execute_query(sql_insercao)
        response = classeBanco.execute_query(sql_selecao)
        response = classeBanco.execute_query(sql_exclusao)
        
        print(sql_insercao)
        print(sql_selecao)
        print(sql_exclusao)
        print("Veiculo Alugado Diariamente com Sucesso! Consulte a Tabela!")

    # #Funcao Alugar o carro Mensalmente
    def alugarVeicMesal(self):
        alugaMensal = self.txt_idVeiculo.text()
        classeBanco = Banco()

        # inserção dos dados na tabela de aluguel
        sql_insercao = f"INSERT INTO alugarVeiculoMensal (id_veiculo) SELECT {alugaMensal} FROM veiculo WHERE id_veiculo = {alugaMensal};"
        
        # selecionando os dados que acabou de ser inserido
        sql_selecao = f"SELECT {alugaMensal} FROM alugarVeiculoMensal;"

        # excluir o veículo da tabela de veículos
        sql_exclusao = f"DELETE FROM veiculo WHERE id_veiculo = {alugaMensal};"

        # Executando a consulta SQL
        response = classeBanco.execute_query(sql_insercao)
        response = classeBanco.execute_query(sql_selecao)
        response = classeBanco.execute_query(sql_exclusao)

        print(sql_insercao)
        print(sql_selecao)
        print(sql_exclusao)
        print("Veiculo Alugado Mensalmente com Sucesso! Consulte a Tabela!")

    # #Funcao para comprar o carro
    def comprarVeic(self):
        comprarVeiculo = self.txt_idVeiculo.text()
        classeBanco = Banco()

        # inserção dos dados na tabela de aluguel
        sql_insercao = f"INSERT INTO comprarVeiculo (id_veiculo) SELECT {comprarVeiculo} FROM veiculo WHERE id_veiculo = {comprarVeiculo};"
        
        # selecionando os dados que acabou de ser inserido
        sql_selecao = f"SELECT {comprarVeiculo} FROM comprarVeiculo;"

        # excluir o veículo da tabela de veículos
        sql_exclusao = f"DELETE FROM veiculo WHERE id_veiculo = {comprarVeiculo};"

        # Executando a consulta SQL
        response = classeBanco.execute_query(sql_insercao)
        response = classeBanco.execute_query(sql_selecao)
        response = classeBanco.execute_query(sql_exclusao)
        
        print(sql_insercao)
        print(sql_selecao)
        print(sql_exclusao)
        print("Veiculo Comprado com Sucesso! Consulte a Tabela!")
# Iniciando a Tela Principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()