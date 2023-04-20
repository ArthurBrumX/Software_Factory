# 55 - Ler 20 números e exibir qual foi o menor e o maior informados.

print ("=" * 60)

print ("*** Contador!! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador_de_numero = 0
    # Nome Da Variável = contador_de_numero.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

maior = 0
    # Nome Da Variável = maior.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

menor = 0
    # Nome Da Variável = menor.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

contador_vezes = 0
    # Nome Da Variável = contador_vezes.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (contador_vezes != 20):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    print ("=" * 60)

    numero = int(input("* Digite Um Numero: "))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    print ("=" * 60)

    contador_de_numero = contador_de_numero + 1
        # Nome Da Variável = contador_de_numero.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador_de_numero + 1

    if (contador_de_numero == 1):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
       
       maior = numero
        # Nome Da Variável = maior.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

       menor = numero
        # Nome Da Variável = menor.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    else:
        # else = seNão
            # Se Nenhuma Condição for Atendida, Execute o Codigo Abaixo.
        
        if numero > maior:
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            maior = numero
                # Nome Da Variável = maior.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        if numero < menor:
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            menor = numero
                # Nome Da Variável = menor.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

    contador_vezes = contador_vezes + 1
        # Nome Da Variável = contador_vezes.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador_vezes + 1


print ("O MAIOR Numero Digitado é: {}".format(maior))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("O MENOR Numero Digitado é: {}".format(menor))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("O ULTIMO Numero Digitado é: {}".format(numero))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("A Quantidade De Números Digitados é: {}".format(contador_de_numero))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)
