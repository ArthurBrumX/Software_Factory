# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

class CaixaMercado:
    def __init__(self, codigoBarras, valorProduto, nomeProduto):
        self.codigosBarras = codigoBarras
        self.valorProduto = valorProduto
        self.nomeProduto = nomeProduto

    def leitorDeCodigoDeBarras(self):
        valorCompra = 0

        self.caixaFiscal = int(input("Digite Codigos Do Produto: "))

        if self.caixaFiscal == 123:
            valorCompra = valorCompra + self.produto_1.valorProduto
        

    def pagar(self):
        pass

    def troco(self):
        pass

