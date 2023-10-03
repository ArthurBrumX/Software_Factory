# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

from ClassesMercado import caixa

print("Super Mercado Cubiculos!")

boasVindas = input("Deseja Comprar [S/N]: ")

while boasVindas == "S" or boasVindas == "s":
    compras = caixa()
    compras.adcionarAoCarrinho

    boasVindas = input("Tem mais alguma coisa [S/N]: ")
    if boasVindas == "N" or boasVindas == "n":
        break
    
imprimir_nomeProduto()



    




















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