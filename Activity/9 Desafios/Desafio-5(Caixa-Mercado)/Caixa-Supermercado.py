# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

from ClassesMercado import novaCompra

comprar = input("Deseja Comprar [S/N]: ")

carrinho = []

while comprar == "S" or comprar == "s":

    if comprar == "S" or comprar == "s":
        novaCompra = novaCompra()

        itens = input("Digite o Nome do Item: ")

        if itens in listaDeItens:
            carrinho.append(listaDeItens)

































# =============================================================================

# from ClassesMercado import produto
# from ClassesMercado import caixa

# print("Super Mercado Cubiculos!")

# comprar = input("Deseja Comprar [S/N]: ")

# carrinho = []

# listaProdutos = produto()

# while comprar == "S" or comprar == "s":
#     carrinho.append(listaProdutos.produto())


    




















# listaProdutos = produto()
# caixa1 = caixa()

# while comprar == "S" or comprar == "s":
#     produto = input("Digite o Nome Do Produto: ")
#     # preco = float(input("Qual o valor do produto: "))
#     carrinho.append(produto)

#     comprar = input("Tem Mais Alguma Coisa [S/N]: ")
#     if comprar == "N" or comprar == "n":
#         break
# print("A Lista de itens é essa: ", carrinho)



    # caixa1.adcionarAoCarrinho(produto)
    # print(carrinho)