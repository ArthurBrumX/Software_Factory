# 61 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

print ("=" * 60)

print ("*** Par Ou Impar ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

impar = 0
    # Nome Da Variável = impar.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

par = 0
    # Nome Da Variável = par.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

for n in range (0, 10):

    numero = int(input("* Digite um numero inteiro: "))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    divisivel = numero % 2
        # Nome Da Variável = divisivel.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> numero % 2

    if (divisivel == 0 ):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        par = par + 1
            # Nome Da Variável = par.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> par + 2


    elif (divisivel == 1):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        impar = impar + 1
            # Nome Da Variável = impar.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> impar + 1

print ("=" * 60)
    
print ("- A Quantidade De Números Par é: {}".format(par))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- A Quantidade De Números Impares é: {}".format(impar))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)









