# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

class produto: # definindo uma classe produto (pois no mercado existem diversos produtos)
    def __init__(self,nome,preco):
        # Principais caracteristicas de um produto
        self.nome = nome 
        self.preco = preco

class CarrinhoDeCompras: # para criar uma lista de compra
    def __init__(self):
        self.itens = [] #lista de itens que vai ter na minha compra

    def adicionarItem(self,produto,quantidade):
        self.itens.append({"Produto":produto, "Quantidade":quantidade})
        
