# 54- Ler diversos números inteiros e exibir quantas vezes o número 50 foi informado. O valor 0 é o código de fim de entrada.

print ("=" * 60)

print ("*** Contador!! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador_50 = 0
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

numero = 1
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (numero != 0):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    numero = int(input("* Digite Um Número: "))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    if (numero != 0):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if (numero == 50):
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            contador_50 = contador_50 + 1
                # Nome Da Variável = contador_50.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> Contador_50 + 1

        elif (numero != 50):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            numero = numero + 1
                # Nome Da Variável = numero.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> numero + 1

print ("=" * 60)

print ("- A Quantidade De Números 50 Digitados é: {} !!".format(contador_50))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

















