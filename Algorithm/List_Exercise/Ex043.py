# 43 - Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, 
# e ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectivaé zero..

verificacao = "sim"

moeda = 50
    # Nome Da Variável = moeda.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

totmoeda = 0
    # Nome Da Variável = totmoeda.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

total = []


while (verificacao != "nao" ):

    verificacao = input("Tem Mais moeda: [S/N]")

    totmoeda += 1

    valor = int(input("Qual o Valor da moeda: R$"))
        # Nome Da Variável = valor.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Entrada De Dados.

    total = valor
        # Nome Da Variável = total.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    total.append(valor)

    if total >= moeda:
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        total += moeda
            # Nome Da Variável = total.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) ->  total - (Valor da Variável: ) ->  moeda 

        totmoeda += 1
            # Nome Da Variável = totmoeda.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) ->  totmoeda - 1


    else:
        # Else = SeNão
            # Se Senhum for verdade, execute o codigo a baixo.
                
        if totmoeda > 0:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print (f"total De {totmoeda} cedulas De R$ {moeda}")
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).


        if moeda == 50:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            moeda = 25
                # Nome Da Variável = moeda.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        elif moeda == 25:
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            moeda = 10
                # Nome Da Variável = moeda.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        elif moeda == 10:
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            moeda = 5
                # Nome Da Variável = moeda.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        elif moeda == 5:
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            moeda = 1
                # Nome Da Variável = moeda.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.
        

verificacao = input("Tem Mais moeda: [S/N]")

print (moeda)
print (totmoeda)