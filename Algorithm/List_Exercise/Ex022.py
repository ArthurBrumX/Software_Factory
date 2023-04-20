# 22 - Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

print ("=" * 60)

print ("*** Supermercado Algoritmo ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Bem-Vindo Cliente Fique a Vontade *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

produto = input("* Digite o Nome Do Produto: ")
    # Nome Da Variável = produto.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

valor = float(input("* Digite o Valor Do Produto R$ "))
    # Nome Da Variável = valor.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

desconto = valor * 10 / 100
    # Nome Da Variável = desconto.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> valor * 10  (Dividido por: ) -> 100

novo_preco = valor - desconto
    # Nome Da Variável = novo_preco.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> valor - (Valor Da Variável: ) -> desconto

print ("-" * 60)

print ("- O Desconto No Produto Foi De: R${}".format(desconto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("-" * 60)

print ("- O Novo Preço Do Produto {} Será De: R${}".format(produto, novo_preco))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("*** Desconto Aplicado Com Sucesso!! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)