from PyQt6 import uic, QTWidgets

import pymysql.connections

banco = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    password = "",
    database = "cadastro275"
)

def funcao_principal():
    codigo = produtos.codigo.text()
    descricao = produtos.descricao.text()
    preco = produtos.preco.text()
    print("Codigo: ",codigo)
    print("Nome: ",descricao)
    print("Valor: ", preco)

    if produtos.limpeza.isChecked():
        print("Categoria Limpeza!")
        categoria = "Limpeza"
    elif produtos.perecivel.isChecked():
        print("Categoria Pereciveis!")
        categoria = "Pereciveis"
    elif produtos.bebida.isChecked():
        print("Categoria Bebidas")
        categoria = "Bebidas"

    # inserindo dados no banco de dados
    cursor = banco.cursor()
    sql = "INSERT INTO produtos(codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)" #colocar dados para inserir no banco
    dados = (str(codigo),str(descricao),str(preco),str(categoria))
    cursor.execute(sql, dados)
    banco.commit()

def listar():
    listarProdutos.show()

    #Mostrar os dados do banco de dados

    cursor = banco.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    listarProdutos.TableWidget.setRowCount(len(dados_recebidos))
    listarProdutos.tableWidget.setColumnCount(5)

    for linha in range(0, len(dados_recebidos)):
        for coluna in range(0,5):
            listaProdutos.tableWidget.setItem(linha,coluna,QTWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))

app = QTWidgets.QApplication([])
produtos = uic.loadUI("#nome do arquivo do qtdesgner") # ele que vai chama a janela pra abrir
produtos.cadastrar.clicked.connect(funcao_principal) # utilizando a funcao principal
produtos.listar.clicked.connect(listar) # ulilizando a funcao listar

produtos.show() #produtos da o seu show
app.exec() #pedindo pra executar
