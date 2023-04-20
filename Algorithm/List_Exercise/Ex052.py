# 52- Ler diversos números e exibir quantos foram digitados.O valor -1 é código de fim de entrada.

print ("=" * 60)

print ("*** Lendo Número ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

pergunta = input("* Deseja Continuar: ")
    # Nome Da Variável = pergunta.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

contador = 0
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

print ("=" * 60)

while (pergunta == "sim"):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo

    numero = float(input("* Digite um numero: "))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    print ("=" * 60)

    if (numero != -1 and pergunta == "sim"):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> soma + (Valor da Variável: ) -> numero


        pergunta = input("* Deseja Continuar: ")
            # Nome Da Variável = pergunta.
            # Tipo Da Variável = Str (String).
            # Função = Entrada De Dados.

    elif (numero == - 1):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("=" * 60)

        print("- A Quantidade De Números digitados é: {}!!".format(contador))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

        print ("=" * 60)

print ("- A Quantidade De Números digitados é: {}!!".format(contador))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)