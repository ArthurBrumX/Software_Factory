# 65 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida

# 1 0
# 3 10
# 6 15
# 9 20
# 12 25

# Exemplo de saída do programa:

# Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela

# R$ 1.000,00 0 1 R$ 1.000,00

print ("=" * 108)

print ("*** Serassa ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 108)

divida = float(input("* Digite o valor inicial da sua divida: "))
    # Nome Da Variável = divida.
    # Tipo Da Variável = float (real).
    # Função = Entrada De Dados.

quant = int(input("* Quantas parcelas: "))
    # Nome Da Variável = quant.
    # Tipo Da Variável = int (Inteiro).
    # Função = Entrada De Dados.

juros = divida * quant / 100
    # Nome Da Variável = juros.
    # Função = Calculo Com Variáveis
     # Calculo: (Valor da Variável: ) -> divida * (Valor da Variável: ) -> quant / 100

total_div = divida + juros
    # Nome Da Variável = total_div.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida + (Valor da Variável: ) -> juro

vezes_3 = divida / 3
    # Nome Da Variável = vezes_3.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida / 3

vezes_6 = divida / 6
    # Nome Da Variável = vezes_6.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida / 6

vezes_9 = divida / 9
    # Nome Da Variável = vezes_9.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida / 9

vezes_12 = divida / 12
    # Nome Da Variável = vezes_12.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida / 12

Juros_10 = divida * 10 / 100
    # Nome Da Variável = Juros_10.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida * 10 /100

Juros_15 = divida * 15 / 100
    # Nome Da Variável = Juros_15.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida * 15 /100

Juros_20 = divida * 20 / 100
    # Nome Da Variável = Juros_20.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida * 20 /100

Juros_25 = divida * 25 / 100
    # Nome Da Variável = Juros_25.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> divida * 25 /100

print ("=" * 108)

print ("- Valor Da Divida   |   Quantidade De Parceclas   |   Valor Da Parcela   |   % De Juros Do valor inicial   |\n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print (f"-    R$ {divida}                 1 x =                     R$ {divida}                     0% = R$ {juros}")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print (f"-    R$ {divida}                 3 x =                     R$ {vezes_3:.2f}                     10% = R$ {Juros_10}")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print (f"-    R$ {divida}                 6 x =                     R$ {vezes_6:.2f}                     15% = R$ {Juros_15}")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print (f"-    R$ {divida}                 9 x =                     R$ {vezes_9:.2f}                     20% = R$ {Juros_20}")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print (f"-    R$ {divida}                12 x =                     R$ {vezes_12:.2f}                     25% = R$ {Juros_25} \n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 108)

print ("*** Total Em Aberto: ***\n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

if (quant == 1):

    print ("- Valor Da Divida   |   Quantidade De Parceclas   |   Valor Da Parcela   |   % De Juros Do valor inicial   |\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print (f"-    R$ {divida}                 1 x =                     R$ {divida}                     0% = R$ {juros}\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (quant == 3):

    print ("- Valor Da Divida   |   Quantidade De Parceclas   |   Valor Da Parcela   |   % De Juros Do valor inicial   |\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print (f"-    R$ {divida}                 3 x =                     R$ {vezes_3:.2f}                   10% = R$ {juros}\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (quant == 6):

    print ("- Valor Da Divida   |   Quantidade De Parceclas   |   Valor Da Parcela   |   % De Juros Do valor inicial   |\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print (f"-    R$ {divida}                 6 x =                     R$ {vezes_6:.2f}                   15% = R$ {juros}\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (quant == 9):

    print ("- Valor Da Divida   |   Quantidade De Parceclas   |   Valor Da Parcela   |   % De Juros Do valor inicial   |\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print (f"-    R$ {divida}                 9 x =                     R$ {vezes_9:.2f}                   20% = R$ {juros}\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (quant == 12):

    
    print ("- Valor Da Divida   |   Quantidade De Parceclas   |   Valor Da Parcela   |   % De Juros Do valor inicial   |\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print (f"-    R$ {divida}                12 x =                     R$ {vezes_12:.2f}                  25% = R$ {juros}\n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 108)