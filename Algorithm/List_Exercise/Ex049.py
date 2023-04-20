# 49 - Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O programa deve solicitar o valor da cotação do dólar.

print ("=" * 60)

print ("*** Conversor! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

dolar = 5.17
    # Nome Da Variável = dolar.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

real = float(input("* Quantos reais seram convertidos: "))
    # Nome Da Variável = preco_produto.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

conversor = real * dolar
    # Nome Da Variável = conversor.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> real * 10 (Valor da Variável: ) -> dolar

print ("=" * 60)

print ("- A cotacao do dolar hoje está em R$ {} !!".format(dolar))
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("- {} reais convertidos são R$ {} dolares!!!".format(real, conversor))
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)









