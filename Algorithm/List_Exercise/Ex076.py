# 76 - Faça um Programaque leia 4 notas, mostre as notas e a média na tela.

print ("=" * 60)

print ("*** Vetor ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

nota_1 = float(input("* Digite Um Número: "))
    # Nome Da Variável = nota_1.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

nota_2 = float(input("* Digite Outro Número: "))
    # Nome Da Variável = nota_2.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

nota_3 = float(input("* Digite Outro Número: "))
    # Nome Da Variável = nota_3.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

nota_4 = float(input("* Digite Outro número: "))
    # Nome Da Variável = nota_4.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

print ("=" * 60)

media = nota_1 + nota_2 + nota_3 + nota_4 / 4
    # Nome Da Variável = media.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> nota_1 + (Valor da Variável: ) -> nota_2 + (Valor da Variável: ) -> nota_3 + (Valor da Variável: ) -> nota_4

print ("- A media desses numeros é: {}".format(media))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)