# 47 - Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

print ("=" * 60)

print ("*** Seja Bem-Vindo! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

valor_1 = int(input("* Digite Um Valor Inteiro: "))
    # Nome Da Variável = valor_1.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

valor_2 = int(input("* Digite Um Valor Inteiro: "))
    # Nome Da Variável = valor_2.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

print ("=" * 60)

if (valor_1 == valor_2):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    soma = valor_1 + valor_2
        # Nome Da Variável = soma.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> valor_1 * (Valor da Variável: ) -> valor_2

    print ("- A Soma Dos Número Digitaod é De: {}".format(soma))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (valor_1 != valor_2):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    Calculo = valor_1 * valor_2
        # Nome Da Variável = calculo.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> valor_1 * (Valor da Variável: ) -> valor_2

    print ("- O Calculo Dos Números Digitaods é De: {}".format(Calculo))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)