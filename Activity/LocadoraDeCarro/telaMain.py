# Form implementation generated from reading ui file 'C:\xampp\htdocs\Projetos\Software_Factory-main\Software_Factory\Activity\LocadoraDeCarro\telaMain.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 527)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QFrame(parent=self.centralwidget)
        self.menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu.setObjectName("menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bnt_home = QtWidgets.QPushButton(parent=self.menu)
        self.bnt_home.setObjectName("bnt_home")
        self.horizontalLayout.addWidget(self.bnt_home)
        self.bnt_cadastrarUser = QtWidgets.QPushButton(parent=self.menu)
        self.bnt_cadastrarUser.setObjectName("bnt_cadastrarUser")
        self.horizontalLayout.addWidget(self.bnt_cadastrarUser)
        self.bnt_cadastrarVeiculo = QtWidgets.QPushButton(parent=self.menu)
        self.bnt_cadastrarVeiculo.setObjectName("bnt_cadastrarVeiculo")
        self.horizontalLayout.addWidget(self.bnt_cadastrarVeiculo)
        self.bnt_listaUser = QtWidgets.QPushButton(parent=self.menu)
        self.bnt_listaUser.setObjectName("bnt_listaUser")
        self.horizontalLayout.addWidget(self.bnt_listaUser)
        self.bnt_listaVeiculo = QtWidgets.QPushButton(parent=self.menu)
        self.bnt_listaVeiculo.setObjectName("bnt_listaVeiculo")
        self.horizontalLayout.addWidget(self.bnt_listaVeiculo)
        self.verticalLayout.addWidget(self.menu)
        self.janelaDeNavegacao = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.janelaDeNavegacao.setObjectName("janelaDeNavegacao")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tituloBoasVindas = QtWidgets.QTextEdit(parent=self.home)
        self.tituloBoasVindas.setObjectName("tituloBoasVindas")
        self.gridLayout_3.addWidget(self.tituloBoasVindas, 0, 0, 1, 1)
        self.janelaDeNavegacao.addWidget(self.home)
        self.page_cadastrarUser = QtWidgets.QWidget()
        self.page_cadastrarUser.setObjectName("page_cadastrarUser")
        self.gridLayout = QtWidgets.QGridLayout(self.page_cadastrarUser)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_cadastroUser = QtWidgets.QFrame(parent=self.page_cadastrarUser)
        self.frame_cadastroUser.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastroUser.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastroUser.setObjectName("frame_cadastroUser")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_cadastroUser)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.layout_nome = QtWidgets.QHBoxLayout()
        self.layout_nome.setObjectName("layout_nome")
        self.string_nome = QtWidgets.QLabel(parent=self.frame_cadastroUser)
        self.string_nome.setObjectName("string_nome")
        self.layout_nome.addWidget(self.string_nome)
        self.txt_nome = QtWidgets.QLineEdit(parent=self.frame_cadastroUser)
        self.txt_nome.setObjectName("txt_nome")
        self.layout_nome.addWidget(self.txt_nome)
        self.gridLayout_5.addLayout(self.layout_nome, 0, 0, 1, 1)
        self.layout_cpf = QtWidgets.QHBoxLayout()
        self.layout_cpf.setObjectName("layout_cpf")
        self.string_cpf = QtWidgets.QLabel(parent=self.frame_cadastroUser)
        self.string_cpf.setObjectName("string_cpf")
        self.layout_cpf.addWidget(self.string_cpf)
        self.txt_cpf = QtWidgets.QLineEdit(parent=self.frame_cadastroUser)
        self.txt_cpf.setObjectName("txt_cpf")
        self.layout_cpf.addWidget(self.txt_cpf)
        self.gridLayout_5.addLayout(self.layout_cpf, 1, 0, 1, 1)
        self.layout_telefone = QtWidgets.QHBoxLayout()
        self.layout_telefone.setObjectName("layout_telefone")
        self.string_telefone = QtWidgets.QLabel(parent=self.frame_cadastroUser)
        self.string_telefone.setObjectName("string_telefone")
        self.layout_telefone.addWidget(self.string_telefone)
        self.txt_telefone = QtWidgets.QLineEdit(parent=self.frame_cadastroUser)
        self.txt_telefone.setObjectName("txt_telefone")
        self.layout_telefone.addWidget(self.txt_telefone)
        self.gridLayout_5.addLayout(self.layout_telefone, 2, 0, 1, 1)
        self.layout_dataNasc = QtWidgets.QHBoxLayout()
        self.layout_dataNasc.setObjectName("layout_dataNasc")
        self.string_dataNasc = QtWidgets.QLabel(parent=self.frame_cadastroUser)
        self.string_dataNasc.setObjectName("string_dataNasc")
        self.layout_dataNasc.addWidget(self.string_dataNasc)
        self.txt_dataNasc = QtWidgets.QLineEdit(parent=self.frame_cadastroUser)
        self.txt_dataNasc.setObjectName("txt_dataNasc")
        self.layout_dataNasc.addWidget(self.txt_dataNasc)
        self.gridLayout_5.addLayout(self.layout_dataNasc, 3, 0, 1, 1)
        self.layout_senha = QtWidgets.QHBoxLayout()
        self.layout_senha.setObjectName("layout_senha")
        self.string_senha = QtWidgets.QLabel(parent=self.frame_cadastroUser)
        self.string_senha.setObjectName("string_senha")
        self.layout_senha.addWidget(self.string_senha)
        self.txt_senha = QtWidgets.QLineEdit(parent=self.frame_cadastroUser)
        self.txt_senha.setObjectName("txt_senha")
        self.layout_senha.addWidget(self.txt_senha)
        self.gridLayout_5.addLayout(self.layout_senha, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_cadastroUser, 1, 0, 1, 1)
        self.frame_bnt_cadastrarUsuario = QtWidgets.QFrame(parent=self.page_cadastrarUser)
        self.frame_bnt_cadastrarUsuario.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bnt_cadastrarUsuario.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bnt_cadastrarUsuario.setObjectName("frame_bnt_cadastrarUsuario")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_bnt_cadastrarUsuario)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.bnt_cadastrarUsuario = QtWidgets.QPushButton(parent=self.frame_bnt_cadastrarUsuario)
        self.bnt_cadastrarUsuario.setObjectName("bnt_cadastrarUsuario")
        self.verticalLayout_23.addWidget(self.bnt_cadastrarUsuario)
        self.gridLayout.addWidget(self.frame_bnt_cadastrarUsuario, 3, 0, 1, 1)
        self.tituloCadastroUser = QtWidgets.QLabel(parent=self.page_cadastrarUser)
        self.tituloCadastroUser.setObjectName("tituloCadastroUser")
        self.gridLayout.addWidget(self.tituloCadastroUser, 0, 0, 1, 1)
        self.frame_cadastroUserMoradia = QtWidgets.QFrame(parent=self.page_cadastrarUser)
        self.frame_cadastroUserMoradia.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastroUserMoradia.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastroUserMoradia.setObjectName("frame_cadastroUserMoradia")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_cadastroUserMoradia)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.layout_pais = QtWidgets.QHBoxLayout()
        self.layout_pais.setObjectName("layout_pais")
        self.string_pais = QtWidgets.QLabel(parent=self.frame_cadastroUserMoradia)
        self.string_pais.setObjectName("string_pais")
        self.layout_pais.addWidget(self.string_pais)
        self.txt_pais = QtWidgets.QLineEdit(parent=self.frame_cadastroUserMoradia)
        self.txt_pais.setObjectName("txt_pais")
        self.layout_pais.addWidget(self.txt_pais)
        self.gridLayout_7.addLayout(self.layout_pais, 0, 0, 1, 1)
        self.layout_cidade = QtWidgets.QHBoxLayout()
        self.layout_cidade.setObjectName("layout_cidade")
        self.string_cidade = QtWidgets.QLabel(parent=self.frame_cadastroUserMoradia)
        self.string_cidade.setObjectName("string_cidade")
        self.layout_cidade.addWidget(self.string_cidade)
        self.txt_cidade = QtWidgets.QLineEdit(parent=self.frame_cadastroUserMoradia)
        self.txt_cidade.setObjectName("txt_cidade")
        self.layout_cidade.addWidget(self.txt_cidade)
        self.gridLayout_7.addLayout(self.layout_cidade, 1, 0, 1, 1)
        self.layout_estado = QtWidgets.QHBoxLayout()
        self.layout_estado.setObjectName("layout_estado")
        self.string_estado = QtWidgets.QLabel(parent=self.frame_cadastroUserMoradia)
        self.string_estado.setObjectName("string_estado")
        self.layout_estado.addWidget(self.string_estado)
        self.txt_estado = QtWidgets.QLineEdit(parent=self.frame_cadastroUserMoradia)
        self.txt_estado.setObjectName("txt_estado")
        self.layout_estado.addWidget(self.txt_estado)
        self.gridLayout_7.addLayout(self.layout_estado, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_cadastroUserMoradia, 2, 0, 1, 1)
        self.janelaDeNavegacao.addWidget(self.page_cadastrarUser)
        self.page_cadastrarVeiculo = QtWidgets.QWidget()
        self.page_cadastrarVeiculo.setObjectName("page_cadastrarVeiculo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_cadastrarVeiculo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tituloCadastroVeiculo = QtWidgets.QLabel(parent=self.page_cadastrarVeiculo)
        self.tituloCadastroVeiculo.setObjectName("tituloCadastroVeiculo")
        self.gridLayout_2.addWidget(self.tituloCadastroVeiculo, 0, 0, 1, 1)
        self.frame_cadastrarVeiculo = QtWidgets.QFrame(parent=self.page_cadastrarVeiculo)
        self.frame_cadastrarVeiculo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastrarVeiculo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastrarVeiculo.setObjectName("frame_cadastrarVeiculo")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_cadastrarVeiculo)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.layout_valorCompra = QtWidgets.QHBoxLayout()
        self.layout_valorCompra.setObjectName("layout_valorCompra")
        self.string_valorCompra = QtWidgets.QLabel(parent=self.frame_cadastrarVeiculo)
        self.string_valorCompra.setObjectName("string_valorCompra")
        self.layout_valorCompra.addWidget(self.string_valorCompra)
        self.txt_valorCompra = QtWidgets.QLineEdit(parent=self.frame_cadastrarVeiculo)
        self.txt_valorCompra.setObjectName("txt_valorCompra")
        self.layout_valorCompra.addWidget(self.txt_valorCompra)
        self.gridLayout_12.addLayout(self.layout_valorCompra, 5, 0, 1, 1)
        self.layout_valorDiario = QtWidgets.QHBoxLayout()
        self.layout_valorDiario.setObjectName("layout_valorDiario")
        self.string_valorDiario = QtWidgets.QLabel(parent=self.frame_cadastrarVeiculo)
        self.string_valorDiario.setObjectName("string_valorDiario")
        self.layout_valorDiario.addWidget(self.string_valorDiario)
        self.txt_valorDiario = QtWidgets.QLineEdit(parent=self.frame_cadastrarVeiculo)
        self.txt_valorDiario.setObjectName("txt_valorDiario")
        self.layout_valorDiario.addWidget(self.txt_valorDiario)
        self.gridLayout_12.addLayout(self.layout_valorDiario, 3, 0, 1, 1)
        self.layout_modelo = QtWidgets.QHBoxLayout()
        self.layout_modelo.setObjectName("layout_modelo")
        self.string_modelo = QtWidgets.QLabel(parent=self.frame_cadastrarVeiculo)
        self.string_modelo.setObjectName("string_modelo")
        self.layout_modelo.addWidget(self.string_modelo)
        self.txt_modelo = QtWidgets.QLineEdit(parent=self.frame_cadastrarVeiculo)
        self.txt_modelo.setObjectName("txt_modelo")
        self.layout_modelo.addWidget(self.txt_modelo)
        self.gridLayout_12.addLayout(self.layout_modelo, 1, 0, 1, 1)
        self.layout_valorMensal = QtWidgets.QHBoxLayout()
        self.layout_valorMensal.setObjectName("layout_valorMensal")
        self.srtring_valorMensal = QtWidgets.QLabel(parent=self.frame_cadastrarVeiculo)
        self.srtring_valorMensal.setObjectName("srtring_valorMensal")
        self.layout_valorMensal.addWidget(self.srtring_valorMensal)
        self.txt_valorMensal = QtWidgets.QLineEdit(parent=self.frame_cadastrarVeiculo)
        self.txt_valorMensal.setObjectName("txt_valorMensal")
        self.layout_valorMensal.addWidget(self.txt_valorMensal)
        self.gridLayout_12.addLayout(self.layout_valorMensal, 4, 0, 1, 1)
        self.layout_cor = QtWidgets.QHBoxLayout()
        self.layout_cor.setObjectName("layout_cor")
        self.string_cor = QtWidgets.QLabel(parent=self.frame_cadastrarVeiculo)
        self.string_cor.setObjectName("string_cor")
        self.layout_cor.addWidget(self.string_cor)
        self.txt_cor = QtWidgets.QLineEdit(parent=self.frame_cadastrarVeiculo)
        self.txt_cor.setObjectName("txt_cor")
        self.layout_cor.addWidget(self.txt_cor)
        self.gridLayout_12.addLayout(self.layout_cor, 2, 0, 1, 1)
        self.layout_marca = QtWidgets.QHBoxLayout()
        self.layout_marca.setObjectName("layout_marca")
        self.string_marca = QtWidgets.QLabel(parent=self.frame_cadastrarVeiculo)
        self.string_marca.setObjectName("string_marca")
        self.layout_marca.addWidget(self.string_marca)
        self.txt_marca = QtWidgets.QLineEdit(parent=self.frame_cadastrarVeiculo)
        self.txt_marca.setObjectName("txt_marca")
        self.layout_marca.addWidget(self.txt_marca)
        self.gridLayout_12.addLayout(self.layout_marca, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_cadastrarVeiculo, 1, 0, 1, 1)
        self.frame_bnt_cadastrarVeiculoo = QtWidgets.QFrame(parent=self.page_cadastrarVeiculo)
        self.frame_bnt_cadastrarVeiculoo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bnt_cadastrarVeiculoo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bnt_cadastrarVeiculoo.setObjectName("frame_bnt_cadastrarVeiculoo")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.frame_bnt_cadastrarVeiculoo)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.bnt_cadastrarVeiculoo = QtWidgets.QPushButton(parent=self.frame_bnt_cadastrarVeiculoo)
        self.bnt_cadastrarVeiculoo.setObjectName("bnt_cadastrarVeiculoo")
        self.verticalLayout_71.addWidget(self.bnt_cadastrarVeiculoo)
        self.gridLayout_2.addWidget(self.frame_bnt_cadastrarVeiculoo, 3, 0, 1, 1)
        self.frame_categoriaVeiculo = QtWidgets.QFrame(parent=self.page_cadastrarVeiculo)
        self.frame_categoriaVeiculo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_categoriaVeiculo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_categoriaVeiculo.setObjectName("frame_categoriaVeiculo")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_categoriaVeiculo)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_categoriaPicapes = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaPicapes.setObjectName("checkBox_categoriaPicapes")
        self.gridLayout_9.addWidget(self.checkBox_categoriaPicapes, 2, 4, 1, 1)
        self.checkBox_categoriaPerua = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaPerua.setObjectName("checkBox_categoriaPerua")
        self.gridLayout_9.addWidget(self.checkBox_categoriaPerua, 3, 1, 1, 1)
        self.checkBox_categoriaFurgao = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaFurgao.setObjectName("checkBox_categoriaFurgao")
        self.gridLayout_9.addWidget(self.checkBox_categoriaFurgao, 3, 4, 1, 1)
        self.checkBox_categoriaSeda = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaSeda.setObjectName("checkBox_categoriaSeda")
        self.gridLayout_9.addWidget(self.checkBox_categoriaSeda, 2, 2, 1, 1)
        self.checkBox_categoriaSuv = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaSuv.setObjectName("checkBox_categoriaSuv")
        self.gridLayout_9.addWidget(self.checkBox_categoriaSuv, 2, 3, 1, 1)
        self.checkBox_categoriaCrossover = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaCrossover.setObjectName("checkBox_categoriaCrossover")
        self.gridLayout_9.addWidget(self.checkBox_categoriaCrossover, 3, 0, 1, 1)
        self.checkBox_categoriaMinivan = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaMinivan.setObjectName("checkBox_categoriaMinivan")
        self.gridLayout_9.addWidget(self.checkBox_categoriaMinivan, 3, 2, 1, 1)
        self.checkBox_categoriaHatch = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaHatch.setObjectName("checkBox_categoriaHatch")
        self.gridLayout_9.addWidget(self.checkBox_categoriaHatch, 2, 1, 1, 1)
        self.checkBox_categoriaEsportivo = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaEsportivo.setObjectName("checkBox_categoriaEsportivo")
        self.gridLayout_9.addWidget(self.checkBox_categoriaEsportivo, 3, 3, 1, 1)
        self.checkBox_categoriaCaminhao = QtWidgets.QCheckBox(parent=self.frame_categoriaVeiculo)
        self.checkBox_categoriaCaminhao.setObjectName("checkBox_categoriaCaminhao")
        self.gridLayout_9.addWidget(self.checkBox_categoriaCaminhao, 2, 0, 1, 1)
        self.frame_tituloCategoriaVeiculo = QtWidgets.QFrame(parent=self.frame_categoriaVeiculo)
        self.frame_tituloCategoriaVeiculo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tituloCategoriaVeiculo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tituloCategoriaVeiculo.setObjectName("frame_tituloCategoriaVeiculo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_tituloCategoriaVeiculo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo_categoriaVeiculo = QtWidgets.QLabel(parent=self.frame_tituloCategoriaVeiculo)
        self.titulo_categoriaVeiculo.setObjectName("titulo_categoriaVeiculo")
        self.verticalLayout_2.addWidget(self.titulo_categoriaVeiculo)
        self.gridLayout_9.addWidget(self.frame_tituloCategoriaVeiculo, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_categoriaVeiculo, 2, 0, 1, 1)
        self.janelaDeNavegacao.addWidget(self.page_cadastrarVeiculo)
        self.page_listaDeUsuarios = QtWidgets.QWidget()
        self.page_listaDeUsuarios.setObjectName("page_listaDeUsuarios")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_listaDeUsuarios)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_bnt_deletarUsuario = QtWidgets.QFrame(parent=self.page_listaDeUsuarios)
        self.frame_bnt_deletarUsuario.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bnt_deletarUsuario.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bnt_deletarUsuario.setObjectName("frame_bnt_deletarUsuario")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_bnt_deletarUsuario)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tituloDigiteID = QtWidgets.QLabel(parent=self.frame_bnt_deletarUsuario)
        self.tituloDigiteID.setObjectName("tituloDigiteID")
        self.horizontalLayout_3.addWidget(self.tituloDigiteID)
        self.txt_DeletarIDUser = QtWidgets.QLineEdit(parent=self.frame_bnt_deletarUsuario)
        self.txt_DeletarIDUser.setObjectName("txt_DeletarIDUser")
        self.horizontalLayout_3.addWidget(self.txt_DeletarIDUser)
        self.bnt_deletarUsuario = QtWidgets.QPushButton(parent=self.frame_bnt_deletarUsuario)
        self.bnt_deletarUsuario.setObjectName("bnt_deletarUsuario")
        self.horizontalLayout_3.addWidget(self.bnt_deletarUsuario)
        self.gridLayout_6.addWidget(self.frame_bnt_deletarUsuario, 1, 0, 1, 1)
        self.tabelaListaDeUsuarios = QtWidgets.QTableWidget(parent=self.page_listaDeUsuarios)
        self.tabelaListaDeUsuarios.setObjectName("tabelaListaDeUsuarios")
        self.tabelaListaDeUsuarios.setColumnCount(9)
        self.tabelaListaDeUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeUsuarios.setHorizontalHeaderItem(8, item)
        self.gridLayout_6.addWidget(self.tabelaListaDeUsuarios, 0, 0, 1, 1)
        self.janelaDeNavegacao.addWidget(self.page_listaDeUsuarios)
        self.page_listaDeVeiculos = QtWidgets.QWidget()
        self.page_listaDeVeiculos.setObjectName("page_listaDeVeiculos")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_listaDeVeiculos)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_btn_OpcoesVeiculos = QtWidgets.QFrame(parent=self.page_listaDeVeiculos)
        self.frame_btn_OpcoesVeiculos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btn_OpcoesVeiculos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btn_OpcoesVeiculos.setObjectName("frame_btn_OpcoesVeiculos")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_btn_OpcoesVeiculos)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tituloDigiteIDveiculo = QtWidgets.QLabel(parent=self.frame_btn_OpcoesVeiculos)
        self.tituloDigiteIDveiculo.setObjectName("tituloDigiteIDveiculo")
        self.horizontalLayout_2.addWidget(self.tituloDigiteIDveiculo)
        self.txt_idVeiculo = QtWidgets.QLineEdit(parent=self.frame_btn_OpcoesVeiculos)
        self.txt_idVeiculo.setObjectName("txt_idVeiculo")
        self.horizontalLayout_2.addWidget(self.txt_idVeiculo)
        self.btn_deletarVeiculo = QtWidgets.QPushButton(parent=self.frame_btn_OpcoesVeiculos)
        self.btn_deletarVeiculo.setObjectName("btn_deletarVeiculo")
        self.horizontalLayout_2.addWidget(self.btn_deletarVeiculo)
        self.btn_alugarDiaria = QtWidgets.QPushButton(parent=self.frame_btn_OpcoesVeiculos)
        self.btn_alugarDiaria.setObjectName("btn_alugarDiaria")
        self.horizontalLayout_2.addWidget(self.btn_alugarDiaria)
        self.btn_alugarMensal = QtWidgets.QPushButton(parent=self.frame_btn_OpcoesVeiculos)
        self.btn_alugarMensal.setObjectName("btn_alugarMensal")
        self.horizontalLayout_2.addWidget(self.btn_alugarMensal)
        self.btn_comprar = QtWidgets.QPushButton(parent=self.frame_btn_OpcoesVeiculos)
        self.btn_comprar.setObjectName("btn_comprar")
        self.horizontalLayout_2.addWidget(self.btn_comprar)
        self.gridLayout_8.addWidget(self.frame_btn_OpcoesVeiculos, 2, 0, 1, 1)
        self.tabelaListaDeVeiculos = QtWidgets.QTableWidget(parent=self.page_listaDeVeiculos)
        self.tabelaListaDeVeiculos.setObjectName("tabelaListaDeVeiculos")
        self.tabelaListaDeVeiculos.setColumnCount(7)
        self.tabelaListaDeVeiculos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaListaDeVeiculos.setHorizontalHeaderItem(6, item)
        self.gridLayout_8.addWidget(self.tabelaListaDeVeiculos, 0, 0, 1, 1)
        self.janelaDeNavegacao.addWidget(self.page_listaDeVeiculos)
        self.verticalLayout.addWidget(self.janelaDeNavegacao)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.janelaDeNavegacao.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bnt_home.setText(_translate("MainWindow", "Home"))
        self.bnt_cadastrarUser.setText(_translate("MainWindow", "Cadastrar Usuario"))
        self.bnt_cadastrarVeiculo.setText(_translate("MainWindow", "Cadastrar Veiculo"))
        self.bnt_listaUser.setText(_translate("MainWindow", "Lista De Usuarios"))
        self.bnt_listaVeiculo.setText(_translate("MainWindow", "Lista De Veiculo"))
        self.tituloBoasVindas.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:36pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">BEM VINDO(A)!!!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">ESCOLHA UMA OPCAO A CIMA!!</span></p></body></html>"))
        self.string_nome.setText(_translate("MainWindow", "Nome"))
        self.string_cpf.setText(_translate("MainWindow", "CPF"))
        self.string_telefone.setText(_translate("MainWindow", "Telefone"))
        self.string_dataNasc.setText(_translate("MainWindow", "Data Nascimento"))
        self.string_senha.setText(_translate("MainWindow", "Senha De Acesso"))
        self.bnt_cadastrarUsuario.setText(_translate("MainWindow", "Cadastrar Usuario"))
        self.tituloCadastroUser.setText(_translate("MainWindow", "                                                                                                          CADASTRAR USUARIO"))
        self.string_pais.setText(_translate("MainWindow", "País"))
        self.string_cidade.setText(_translate("MainWindow", "Cidade"))
        self.string_estado.setText(_translate("MainWindow", "Estado"))
        self.tituloCadastroVeiculo.setText(_translate("MainWindow", "                                                                                                           CADASTRAR VEICULO"))
        self.string_valorCompra.setText(_translate("MainWindow", "Valor Da Compra"))
        self.string_valorDiario.setText(_translate("MainWindow", "Valor Diario"))
        self.string_modelo.setText(_translate("MainWindow", "Modelo"))
        self.srtring_valorMensal.setText(_translate("MainWindow", "Valor Mensal"))
        self.string_cor.setText(_translate("MainWindow", "Cor"))
        self.string_marca.setText(_translate("MainWindow", "Marca"))
        self.bnt_cadastrarVeiculoo.setText(_translate("MainWindow", "Cadastrar Veiculo"))
        self.checkBox_categoriaPicapes.setText(_translate("MainWindow", "Picapes"))
        self.checkBox_categoriaPerua.setText(_translate("MainWindow", "Perua "))
        self.checkBox_categoriaFurgao.setText(_translate("MainWindow", "Furgão"))
        self.checkBox_categoriaSeda.setText(_translate("MainWindow", "Sedã"))
        self.checkBox_categoriaSuv.setText(_translate("MainWindow", "SUV"))
        self.checkBox_categoriaCrossover.setText(_translate("MainWindow", "Crossover"))
        self.checkBox_categoriaMinivan.setText(_translate("MainWindow", "Minivan"))
        self.checkBox_categoriaHatch.setText(_translate("MainWindow", "Hatch"))
        self.checkBox_categoriaEsportivo.setText(_translate("MainWindow", "Esportivo"))
        self.checkBox_categoriaCaminhao.setText(_translate("MainWindow", "Caminhão"))
        self.titulo_categoriaVeiculo.setText(_translate("MainWindow", "CATEGORIA DO VEICULO"))
        self.tituloDigiteID.setText(_translate("MainWindow", "Digite o ID Que Deseja Deletar: "))
        self.bnt_deletarUsuario.setText(_translate("MainWindow", "Deletar Usuario"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TELEFONE"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DATA NASC"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PAIS"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ESTADO"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CIDADE"))
        item = self.tabelaListaDeUsuarios.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "SENHA"))
        self.tituloDigiteIDveiculo.setText(_translate("MainWindow", "Digite o ID Do Veiculo Desejado: "))
        self.btn_deletarVeiculo.setText(_translate("MainWindow", "Deletar Veiculo"))
        self.btn_alugarDiaria.setText(_translate("MainWindow", "Alugar Diaria"))
        self.btn_alugarMensal.setText(_translate("MainWindow", "Alugar Mensal"))
        self.btn_comprar.setText(_translate("MainWindow", "Realizar Compra Do Veiculo"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CATEGORIA"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MARCA"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MODELO"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "VALOR(DIARIO)"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "VALOR(MENSAL)"))
        item = self.tabelaListaDeVeiculos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "VALOR(COMPRA)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
