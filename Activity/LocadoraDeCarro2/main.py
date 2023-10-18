from Crud.Create import *
from Crud.Delete import *
from Crud.Read import *
from Crud.Update import *
#importa 
#from pasta1 import arquivo1

import pymysql.connections

#importando as Bibliotecas que seram usadas
from PyQt6.QtWidgets import QApplication, QMainWindow
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



# Iniciando a Tela Principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = telaPrincipal()
    window.show()
    app.exec()