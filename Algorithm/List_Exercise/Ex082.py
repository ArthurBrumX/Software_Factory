# 82 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

print ("=" * 60)

print ("*** Par Ou Impar ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

par = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

impar = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

contador = 1
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

print ("- Digite 10 Números Inteiro! ")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

while (contador < 11):

    numero = int(input("* Digite o {}° Numero:  ".format(contador)))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    print ("=" * 60)

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    calculo = numero % 2
        # Nome Da Variável = calculo.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> numero % 2

    if (calculo == 0):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        par.append(numero)
            # Append = Acrecentar

    elif (calculo == 1):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        impar.append(numero)
            # Append = Acrecentar

print ("=" * 60)

print ("- Os Números Pares Digitados São: {}".format(par))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Os Números Impares Digitados São: {}".format(impar))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

