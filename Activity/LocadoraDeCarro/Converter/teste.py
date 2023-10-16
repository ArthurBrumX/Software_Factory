# nao funcionou
# tentar outro


# metodo para inserir um usuario no  banco
# def inserirUsuario(self,nome,cpf,telefone,data_Nasc,senha_Acess,pais,cidade,estado):
#     nome = self.txt_nome.text()
#     cpf = self.txt_cpf.text()
#     telefone = self.txt_telefone.text()
#     data_Nasc = self.txt_dataNasc.text()
#     senha_Acess = self.txt_senha.text()
#     pais = self.txt_pais.text()
#     cidade = self.txt_cidade.text()
#     estado = self.txt_estado.text()
#     try:
#         cursor = self.conexao.cursor()
#         cursor.execute("""
#             INSERT INTO usuarios(nome,cpf,telefone,data_Nasc,senha_Acess,pais,cidade,estado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
#         """,(nome,cpf,telefone,data_Nasc,senha_Acess,pais,cidade,estado))

#         self.conexao.commit() 
#         print("Usuario Adcionado!")   

#     except AttributeError:
#         print("Faça a Conexao!")