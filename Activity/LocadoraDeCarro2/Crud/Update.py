import Create

class Update:
    def __init__(self) -> None:
        pass

    #Funcao para cadastrar o usuario
    def inserirUsuario(self): 
        nome = self.txt_nome.text()
        cpf = self.txt_cpf.text()
        tel = self.txt_telefone.text()
        nasc = self.txt_dataNasc.text()
        senha = self.txt_senha.text()
        pais = self.txt_pais.text()
        cidade = self.txt_cidade.text()
        estado = self.txt_estado.text()
        classeBanco = Create()
       
        sql = f"INSERT INTO usuario(nome,cpf,telefone,nasc,senha,pais,cidade,estado) VALUES('{nome}','{cpf}','{tel}','{nasc}','{senha}','{pais}','{cidade}','{estado}')"
        response = classeBanco.execute_query(sql)
        print(sql)

    #Funcao para cadastrar o veiculo
    def cad_veiculo(self):
    
        valorCompra = self.txt_valorCompra.text()
        diario = self.txt_valorDiario.text()
        mod = self.txt_modelo.text()
        mensal = self.txt_valorMensal.text()
        cor = self.txt_cor.text()
        marca = self.txt_marca.text()                                                          
        classeBanco = Create()

        sql = f"INSERT INTO veiculo(marca, modelo,cor,valor_diario,valor_mensal,valor_compra) VALUES('{marca}','{mod}','{cor}','{diario}','{mensal}','{valorCompra}')"
        response = classeBanco.execute_query(sql)
        print(sql)   