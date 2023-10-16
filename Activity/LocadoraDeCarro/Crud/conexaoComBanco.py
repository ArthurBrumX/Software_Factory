import psycopg2
import pymysql.connections
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

def conexaoBancoDados():
    try:
        # Conectando com o bacno
        def conexao_banco(self):
            self.conexao = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = '12345',
                database = 'LocadoraDeCarros',
                port = '5432'
            )

            print(self.conexao.info)
            print(self.conexao.status)
            self.cursor = self.conexao.cursor()

    except Exception as erro:
        print(erro)

# Iniciando a classe
if __name__ == "__main__":
    db = conexaoBancoDados()