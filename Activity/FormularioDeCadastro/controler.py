from PyQt6 import uic, QtWidgets
import pymysql.connections
# pip install pymysql

numero_id=0

#para poder se conectar com o banco de dados
banco = pymysql.connections.Connection(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro275"
)

def funcao_principal():
    codigo = produtos.codigo.text()
    descricao = produtos.descricao.text()
    preco = produtos.preco.text()
    print("Identificacao:", codigo)
    print("Nome:", descricao)
    print("Valor:", preco)

    if produtos.limpeza.isChecked():
        print("Categoria Limpeza")
        categoria="Limpeza"
    elif produtos.perecivel.isChecked():
        print("Categoria Perecível")
        categoria="Perecível"
    elif produtos.bebida.isChecked():
        print("Categoria Bebidas")
        categoria="Bebidas"
    
    #Inserindo dados no banco de dados
    cursor = banco.cursor()
    sql = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(codigo),str(descricao), str(preco), categoria)
    cursor.execute(sql, dados)
    banco.commit()


def listar():
    listarProdutos.show()
    
    #Mostrar os dados do banco de dados
    cursor = banco.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    dados_recebido = cursor.fetchall()

    listarProdutos.tableWidget.setRowCount(len(dados_recebido))
    listarProdutos.tableWidget.setColumnCount(5)

    for linha in range(0,len(dados_recebido)):
        for coluna in range (0,5):
            listarProdutos.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebido[linha][coluna])))

def excluir_dados():
    linha = listarProdutos.tableWidget.currentRow()
    listarProdutos.tableWidget.removeRow(linha)

    #quero remover do banco de dados tambem
    cursor = banco.cursor()
    cursor.execute("SELECT id_produtos FROM produtos")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id_produtos" + str(valor_id))
    banco.commit()

def editar_dados():
    global numero_id
    linha = listarProdutos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id_produtos FROM produtos")
    dados_recebidos = cursor.fetchall()
    valor_id = dados_recebidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id_produtos" + str(valor_id))
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produtos[0][0]))
    tela_editar.codigo.setText(str(produtos[0][1]))
    tela_editar.descricao.setText(str(produtos[0][2]))
    tela_editar.preco.setText(str(produtos[0][3]))
    tela_editar.categoria.setText(str(produtos[0][4]))

    numero_id = valor_id

app = QtWidgets.QApplication([])
produtos = uic.loadUi("cadastro_produtos.ui")
listarProdutos = uic.loadUi("listar_dados.ui")
produtos.cadastrar.clicked.connect(funcao_principal)
produtos.listar.clicked.connect(listar)
listarProdutos.Deletar.clicked.connect(excluir_dados)
listarProdutos.editar.clicked.connect(editar_dados)

tela_editar = uic.load_ui("modal_editar.ui")
tela_editar.salvar.clicked.connect(salvar_dados_editados)

produtos.show()
app.exec()

# pra chamar uma variavel dentro de uma funcao, tem q atribuir o valor a uma variavel nova e coloca nome da variavel.funcao

#novaVariavel = nomeDavariavel.funcao