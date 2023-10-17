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
from PyQt6 import QApplication, QMainWindow,QtWidgets
from telaMain import Ui_MainWindow
import pymysql
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

        # Executando Fucnoes
        self.bnt_cadastrarUsuario.clicked.connect(self.inserirUsuario)
        self.bnt_cadastrarVeiculoo.clicked.connect(self.cad_veiculo)
        self.bnt_deletarUsuario.clicked.connect(self.deletar_usuario)
        self.btn_deletarVeiculo.clicked.connect(self.deletar_veiculo)
        self.bnt_listaUser.clicked.connect(self.listarNaTela)

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

    # #Funcao para deletar Usuario
    def deletar_usuario(self):

        deletarUser = self.txt_DeletarIDUser.text()
        classeBanco = Banco()

        sql = f"DELETE FROM usuario WHERE id_usuario = {deletarUser}"
        response = classeBanco.execute_query(sql)
        print(sql)

    # Funcao para deletar veiculo
    def deletar_veiculo(self):

        deletarVeic = self.txt_idVeiculo.text()
        classeBanco = Banco()

        sql = f"DELETE FROM veiculo WHERE id_veiculo = {deletarVeic}"
        response = classeBanco.execute_query(sql)
        print(sql)

    # Funcao para listar clientes
    def listarNaTela(self):
        #Mostrar os dados do banco de dados

        classeBanco = Banco()
        sql = "SELECT * FROM usuario"
        response = classeBanco.execute_query(sql)
        print(response)

        for usuario in response:
            item = QtWidgets.QTreeWidgetItem()
            item.setText(0, str(usuario["id"]))  # Define o ID do usuário na primeira coluna
            item.setText(1, usuario["nome"])  # Define o nome do usuário na segunda coluna
            item.setText(2, usuario["email"])  # Define o email do usuário na terceira coluna

        for linha in range(0,len(response)):
            for coluna in range (0,9):
                window.tabelaListaDeUsuarios.setItem(linha,coluna,QtWidgets.QTreeWidget(str(response[linha][coluna])))
   

# Iniciando a Tela Principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()