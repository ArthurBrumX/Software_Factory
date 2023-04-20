# 26 - Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição: Se o preço de aquisição de um produto é menor 
# que R$ 50,00, ele deve ser vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, faça um algoritmo que leia o valor de aquisição de um produto 
# e mostre o seu valor de venda.

print ("=" * 60)

print ("*** Brechó Tengen Uzui ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("** Caixa **")
    # Apresentação Ao Usuário.

print ("=" * 60)

valor_produto = float(input("* Qual o Valor Do Produto: "))
    # Nome Da Variável = valor_produto.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

if (valor_produto < 50):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    reajuste = (valor_produto * 30) / 100
        # Nome Da Variável = reajuste.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) ->valor_produto * 30 (Dividido Por:) / 100

    print ("- O lucro Desta Venda Foi De R${} Reais!!".format(reajuste))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (valor_produto >= 50):
        # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    reajuste = (valor_produto * 45) / 100
        # Nome Da Variável = reajuste.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) ->valor_produto * 45 (Dividido Por:) / 100

    total = valor_produto + reajuste
    # Nome Da Variável = total_p.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> c_pequenas * (Valor Da Variável: ) -> p

    print ("- O Valor Do Produto Passa-rá a Ser De R$ {} Reais!!".format(total))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).


print ("=" * 60)

print ("*** Fim Da Compra ***")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("*** Volte Sempre ***")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)