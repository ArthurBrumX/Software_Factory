# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

class caixa: # controla saida de produtos
    def __init__(self):
        self.nome = input("Digite o Nome Do Produto: ")
        self.valor = input("Digite o Valor do produto: ")
        self.nomeProduto = []
        self.valorProduto = []

    def adcionarAoCarrinho(self,produto,quantidade,valor):
        self.nomeProduto.append((produto,quantidade))
        self.valorProduto.append((valor))
        
    def imprimir_nomeProduto(self):
        for nome in self.nomeProduto:
            print(nome)


    # def passarNoCaixa(self):
    #     valorCompra = 0
    #     for produto, quantidade in self.nomeProduto:
    #         valorCompra += produto.preco * quantidade
        
    #     return valorCompra

    # def pagar(self, valorPago):
    #     valorCompra = self.passarNoCaixa()
    #     troco = valorPago - valorCompra
    #     if troco >= 0:
    #         self.imprimirRecibo(valorCompra, troco)
    #         self.carrinho = []
    #     else:
    #         print("Valor pago insuficiente, adicione mais dinheiro")
        
    # def imprimir_recibo(self, total, troco):
    #     print("Recibo de Compra")
    #     print("================")
    #     for produto, quantidade in self.produtos_comprados:
    #         print(f"{produto.nome}: {quantidade} x R${produto.preco:.2f}")
    #     print("================")
    #     print(f"Total: R${total:.2f}")
    #     print(f"Troco: R${troco:.2f}")
    #     print("================")


