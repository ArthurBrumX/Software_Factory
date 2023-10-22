
        # deletarUsuario = self.bnt_deletarUsuario.text()                                                       
        # classeBanco = Banco()

        # sql = f"DELETE FROM usuario WHERE nome = '{deletarUsuario}'"
        # response = classeBanco.execute_query(sql)
        # print(sql)

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

