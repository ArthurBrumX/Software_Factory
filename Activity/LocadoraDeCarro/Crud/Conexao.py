import psycopg2
import pymysql.connections
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit


def conexao_banco():
    conexao = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = '12345',
    database = 'LocadoraDeCarros',
    port = '5432'
    )

    print(conexao.info)
    print(conexao.status)


    cursor = conexao.cursor()

    #crud

    cursor.close()
    conexao.close()

class CadastroClienteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configurar widgets e layout aqui
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Cadastro de Cliente")

        # Exemplo de como conectar um botão a uma função
        self.btn_cadastrar = QPushButton("Cadastrar", self)
        self.btn_cadastrar.clicked.connect(self.cadastrar_cliente)

    def cadastrar_cliente(self):
        # Função para pegar dados dos campos e inserir no banco de dados
        nome = self.lineEdit_nome.text()
        sobrenome = self.lineEdit_sobrenome.text()
        # Inserir no banco de dados (você precisará implementar esta parte)

def main():
    app = QApplication(sys.argv)
    ex = CadastroClienteApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    