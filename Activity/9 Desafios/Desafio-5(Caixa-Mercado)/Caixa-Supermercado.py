# 5 - Desenvolva um sistema simulando um caixa de supermercado em Python, utilizando 
# Programação Orientada a Objetos (POO). 
# O sistema deve permitir a realização de compras, cálculo de total e troco. 

from ClassesMercado import CaixaMercado

produto_1 = CaixaMercado(123,4.50,"Bolacha")
produto_2 = CaixaMercado(456,3.21,"Trigo")
produto_3 = CaixaMercado(789,4.22,"Agua Sanitaria")
produto_4 = CaixaMercado(101112,5.23,"Suco")
produto_5 = CaixaMercado(1131415,6.24,"Café")
produto_6 = CaixaMercado(161718,7.25,"Papel Higienico")
produto_7 = CaixaMercado(192021,8.26,"Leite")
produto_8 = CaixaMercado(222324,9.27,"Arroz")
produto_9 = CaixaMercado(252627,10.28,"Cereal")
produto_10 = CaixaMercado(282930,11.29,"Bolo")

print("Super Mercado xingling")

quantProdutos = input("Tem Produto [S/N]: ")
while quantProdutos == "S" or quantProdutos == 's':
        leitorCodigoBarras = int(input("Digite Codigos Do Produto: "))
        if leitorCodigoBarras == 123:
            produto_1.passarCompra()


