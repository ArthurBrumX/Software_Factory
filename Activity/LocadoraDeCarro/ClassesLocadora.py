# O aluno deverá desenvolver uma aplicação em Python utilizando PyQt ou PySide, 
# para uma locadora de veículos, comunicando com o banco de dados no qual deverá ter as seguintes funcionalidades: 

# - Opções para locar o carro por diária 
# - Opções para locar o carro mensalista 
# - Opções de compra do carro 

# Categorias (aluguel-diario, compra, Mensalista)

# O sistema deverá permitir cadastrar os veículos e em qual categoria ele se enquadra. 
# (Cadastrar, R(mostrar os dados), U(editar os dados), D(deletar se o carro nunca foi alugado ou vendido)). 
# Cadastrar usuário para realizar a venda ou a locação. 

from Crud import Conexao # para importar uma classe de outro arquivo
#from pasta1 import arquivo1

import pymysql.connections

#importando as Bibliotecas que seram usadas
from PyQt6.QtWidgets import QApplication, QMainWindow
from arquivo import Ui_MainWindow
import sys

# Criando um instaciamento (chamando o banco)
conexao = Conexao.conexao_banco()

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
    
# Iniciando a Tela Principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()