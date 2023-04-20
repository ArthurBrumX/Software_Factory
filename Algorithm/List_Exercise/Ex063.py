# 63 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

print ("=" * 60)

print ("*** Calculo! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador_numero = 0
    # Nome Da Variável = contador_numero.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

maior = 0
    # Nome Da Variável = maiorr.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

menor = 0
    # Nome Da Variável = menor.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

soma = 0
    # Nome Da Variável = soma.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

cal = 0
    # Nome Da Variável = cal.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

continuar = "Sim"
    # Nome Da Variável = continuar.
    # Tipo Da Variavel = Str (String).
    # Função = Atribuição De Valor.

while (continuar == "Sim") or (continuar == "sim"):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    numero = float(input("* Digite Um Número: "))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    print ("=" * 60)

    contador_numero = contador_numero + 1
        # Nome Da Variável = contador_numero.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador_numero + 1

    if (contador_numero == 1):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        maior = numero
            # Nome Da Variável = maior.
            # Tipo Da Variavel = Float (Real).
            # Função = Atribuição De Valor.

        menor = numero
            # Nome Da Variável = menor.
            # Tipo Da Variavel = Float (Real).
            # Função = Atribuição De Valor.
    
    else:
        # else = seNão
            # Se Nenhuma Condição for Atendida, Execute o Codigo Abaixo.

        if (numero > maior):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

            maior = numero
                # Nome Da Variável = maior.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        if (numero < menor):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

            menor = numero
                # Nome Da Variável = menor.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

    soma = soma + numero
        # Nome Da Variável = soma.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> soma + (Valor da Variável: ) -> numero

    cal = menor + maior
        # Nome Da Variável = cal.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> menor + (Valor da Variável: ) -> maior

    continuar = input("Deseja Continuar: [S/N] ")
        # Nome Da Variável = Continuar.
        # Tipo Da Variável = Str (String).
        # Função = Entrada De Dados.

print ("=" * 60)

print ("O Maior Valor Digitado é: {}".format(maior))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("O Menor Valor Digitado é: {}".format(menor))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("O Resultado Da Soma De Todos Numeros é: {}".format(soma))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("A Soma Entre o Maior Numero Digitado e o Menor é: {}".format(cal))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)











