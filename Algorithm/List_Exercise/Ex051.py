# 51 - Ler diversos números e exibir qual foi a soma. O valor -999 é o código de fim da entrada.

print ("=" * 60)

print ("*** Somando Numeros ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

pergunta = input("* Deseja Continuar: ")
    # Nome Da Variável = pergunta.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

soma = 0
    # Nome Da Variável = soma.
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

    if (numero != -999 and pergunta == "sim"):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        soma = soma + numero
            # Nome Da Variável = soma.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> soma + (Valor da Variável: ) -> numero


        pergunta = input("* Deseja Continuar: ")
            # Nome Da Variável = pergunta.
            # Tipo Da Variável = Str (String).
            # Função = Entrada De Dados.

    elif (numero == - 999):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("=" * 60)

        print("- A soma dos numeros é: {}!!".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

        print ("=" * 60)

print ("- A soma dos numero é: {}!!".format(soma))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

