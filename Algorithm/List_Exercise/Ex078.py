# 78 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

print ("=" * 60)

print ("*** Par Ou Impar ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

impar = []
    #Vetor
        # Comando para armazenar informacoes como uma lista

par = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

numero = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

for c in range (0, 5):

    digito = int(input("* Digite Um Numero Inteiro: "))
        # Nome Da Variável = primeiro.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    divisao = digito % 2
        # Nome Da Variável = contvogal.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contvogal + 1

    numero.append(digito)
        # Append = Acrecentar

    if (divisao == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        par.append(digito)
            # Append = Acrecentar

    elif (divisao == 1):
        # elIf = SeNão Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        impar.append(digito)
            # Append = Acrecentar

print ("=" * 60)

print ("- O Numeros Digitados Impares o: {}".format(impar))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Numeros Digitados pares São: {}".format(par))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Numeros Digitados Sao: {}".format(numero))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)



