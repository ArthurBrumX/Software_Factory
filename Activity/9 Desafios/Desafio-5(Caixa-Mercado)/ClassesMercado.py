# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

class novaCompra:
    def __init__(self):
        pass
        self.listaDeItens = [
            [Arroz = 15],
            [Feijao = 5.50],
            [Açucar = 9.90],
            [Macarrao = 3.50],
            [Suco = 0.99],
            [Refrigerante = 5.50]
        ]

    def private





























# ==============================================================================

# class novaCompra:
#     def __init__(self):
#         self.carrinho = []
#         self.produtosDoMercado = [
#             ["Arroz", 15],
#             ["Feijao", 5.50],
#             ["Açucar", 9.90],
#             ["Macarrao", 3.50],
#             ["Suco", 0.99],
#             ["Refrigerante", 5.50]
#         ]
#     class caixa: # controla saida de produtos
#         def __init__(self):
#             pass

#         def adcionarAoCarrinho(self,produto,quantidade):
#             self.produto = input("Qual o Nome Do Produto: ")
#             self.quantidade = int(input("Quantos Vai Querer: "))
#             if produto in self.produtosDoMercado:
#                 self.carrinho.append((produto))

#         def passarNoCaixa(self):
#             valorCompra = 0
#             if produto in self.produtosDoMercado:
#                 valorCompra += self.produtosDoMercado[1] * quantidade
            
#             return valorCompra

#         def pagar(self, valorPago):
#             valorCompra = self.passarNoCaixa()
#             troco = valorPago - valorCompra
#             if troco >= 0:
#                 self.imprimirRecibo(valorCompra, troco)
#                 self.carrinho = []
#             else:
#                 print("Valor pago insuficiente, adicione mais dinheiro")
            
#         def imprimir_recibo(self, total, troco):
#             print("Recibo de Compra")
#             print("================")
#             for produto, quantidade in self.produtos_comprados:
#                 print(f"{produto.nome}: {quantidade} x R${produto.preco:.2f}")
#             print("================")
#             print(f"Total: R${total:.2f}")
#             print(f"Troco: R${troco:.2f}")
#             print("================")


# ==============================================================================


# class produto: # controlar os produtos
#     def __init__(self):
#         self.nome = input("Digite o Nome Do Produto")
#         self.valor = input("Digite o Valor do produto")

# class caixa: # controla saida de produtos
#     def __init__(self):
#         self.carrinho = []

#     def adcionarAoCarrinho(self,produto,quantidade):
#         self.carrinho.append((produto,quantidade))

#     def passarNoCaixa(self):
#         valorCompra = 0
#         for produto, quantidade in self.carrinho:
#             valorCompra += produto.preco * quantidade
        
#         return valorCompra

#     def pagar(self, valorPago):
#         valorCompra = self.passarNoCaixa()
#         troco = valorPago - valorCompra
#         if troco >= 0:
#             self.imprimirRecibo(valorCompra, troco)
#             self.carrinho = []
#         else:
#             print("Valor pago insuficiente, adicione mais dinheiro")
        
#     def imprimir_recibo(self, total, troco):
#         print("Recibo de Compra")
#         print("================")
#         for produto, quantidade in self.produtos_comprados:
#             print(f"{produto.nome}: {quantidade} x R${produto.preco:.2f}")
#         print("================")
#         print(f"Total: R${total:.2f}")
#         print(f"Troco: R${troco:.2f}")
#         print("================")


