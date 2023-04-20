# 62 - Faça um programaque calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

print ("=" * 60)

print ("*** Fatorial ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

numero = int(input("Fatorial de: "))
    # Nome Da Variável = numero.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

print ("=" * 60)

resultado = 1
    # Nome Da Variável = resultado.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

count = 1
    # Nome Da Variável = count.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (count <= numero):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.
    
    resultado = resultado * count
        # Nome Da Variável = resultado.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> resultado * (Valor da Variável: ) -> count

    count = count + 1
        # Nome Da Variável = count.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> count + 1

print ("=" * 60)

print ("O Fatorial De {}, é Igual a: {}".format(numero, resultado))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

