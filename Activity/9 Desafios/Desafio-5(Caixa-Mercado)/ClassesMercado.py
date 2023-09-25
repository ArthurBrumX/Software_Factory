# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

class CaixaMercado:
    def __init__(self, leitorCodigoBarras, valorProduto, produto, valorCompra):
        self.leitorCodigoBarras = leitorCodigoBarras
        self.valorProduto = valorProduto
        self.produto = produto
        self.valorCompra = valorCompra

    def passarCompra(self):
        self.valorCompra = self.valorCompra + self.valorProduto

    def pagar(self):
        pass

    def troco(self):
        pass

