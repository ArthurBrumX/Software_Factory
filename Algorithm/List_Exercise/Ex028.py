# 28 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# • o produto do dobro do primeiro com metade do segundo .
# • a soma do triplo do primeiro com o terceiro.
# • o terceiro elevado ao cubo.


print ("=" * 60)

print ("*** Calculo! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Olá Usuário, Vamos Realizar Alguns Calculos!!! *")
print ("* Preencha Os Campos Abaixo Para Descobri-los! * ")
    # Apresentação Ao Usuário.

print ("=" * 60)

n1 = int(input("* Digite Um Número Inteiro: "))
    # Nome Da Variável = n1.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

n2 = int(input("* Digite Um Número Inteiro: "))
    # Nome Da Variável = n2.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

n3 = float(input("* Digite Um Numero Real: "))
    # Nome Da Variável = n3.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Entrada De Dados.

dobro = n1 * 2
    # Nome Da Variável = dobro.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> n1 * 2

metade = n2 / 2
    # Nome Da Variável = metade.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> n2 / 2

resultado = dobro + metade
    # Nome Da Variável = resultado.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> dobro + (Valor da Variável: ) -> metade

triplo = n1 * 3
    # Nome Da Variável = triplo.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> n1 * 3

resultado_2 = triplo + n3
    # Nome Da Variável = resultado_2.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> triplo + (Valor da Variável: ) -> n3

expoente = n3 ^ 3
    # Nome Da Variável = expoente.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> n3 ^ 3

print ("- O Produto Do Dobro Do Primeiro Com Metade Do Segundo Resulta em: {}!".format(resultado)) # 1° pergunta
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A Soma Do Triplo Do Primeiro Com o Terceiro Resulta Em: {}!".format(resultado_2)) # 2° pergunta
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Terceiro Elevado Ao Cubo é: {}!".format(expoente)) # 3° pergunta
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)