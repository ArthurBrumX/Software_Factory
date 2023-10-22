import Banco

class Delete:
    def __init__(self) -> None:
        pass

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

        sql = f"DELETE FROM veiculo WHERE id_veiculo = {deletarVeic}" # uma variavel que contem um comando sql
        response = classeBanco.execute_query(sql) # execute_query() - executa um comando sql
        print(sql)