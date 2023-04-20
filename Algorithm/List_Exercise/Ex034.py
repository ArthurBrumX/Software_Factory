# 34 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# • Álcool:

    # • até 20 litros, desconto de 3% por litro

    # • acima de 20 litros, desconto de 5% por litro

# • Gasolina:

    # • até 20 litros, desconto de 4% por litro

    # • acima de 20 litros, desconto de 6% por litro

# • Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser 
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90

print ("=" * 60)

print ("*** Posto Wakanda Forever ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

alcool = 1.90
    # Nome Da Variável = alcool.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

gasolina = 2.50
    # Nome Da Variável = gasolina.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

print ("* [A] -> álcool")
    # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

print ("* [G] -> Gasolina")
    # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

tipo = input("* Qual Tipo De Combustivel irá Querer: ")
    # Nome Da Variável = n1.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

if (tipo == "A") or (tipo == "a"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    litros = float(input("* Quantos Litros voce vai querer: "))
        # Nome Da Variável = litros.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.
    
    print ("=" * 60)

    if (litros <= 20):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        desconto = litros * 3 / 100
            # Nome Da Variável = desconto.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros * 3 ( Dividido por: ) -> / 100

        total = litros - desconto
            # Nome Da Variável = total.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros - (Valor Da Variável: ) -> desconto.

        print ("- O total a Pagar é De: R$ {}".format(total))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (litros > 20 ):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        desconto = litros * 5 / 100
            # Nome Da Variável = desconto.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros * 5 ( Dividido por: ) -> / 100

        total = litros - desconto
            # Nome Da Variável = total.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros - (Valor Da Variável: ) -> desconto.

        print ("- O total a Pagar é De: R$ {}".format(total))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).


elif (tipo == "G") or (tipo == "g"):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    litros = float(input("- Quantos Litros voce vai querer: "))
        # Nome Da Variável = litros.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    print ("=" * 60)

    if (litros <= 20):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        desconto = litros * 4 / 100
            # Nome Da Variável = desconto.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros * 4 ( Dividido por: ) -> / 100

        total = litros - desconto
            # Nome Da Variável = total.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros - (Valor Da Variável: ) -> desconto.

        print ("- O Total a Pagar é De: R$ {}".format(total))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (litros > 20):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        desconto = litros * 6 / 100
            # Nome Da Variável = desconto.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros * 6 ( Dividido por: ) -> / 100

        total = litros - desconto
            # Nome Da Variável = soma.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> litros + (Valor Da Variável: ) -> desconto.

        print ("- O total a Pagar é de: R$ {}".format(total))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

print ("=" * 60)
            











