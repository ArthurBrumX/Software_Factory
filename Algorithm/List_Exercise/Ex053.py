# 53 - Ler diversos números e exibir quantos números ímpares foram digitados. Considere o valor - 999 como código fim de entrada.

print ("=" * 60)

print ("*** Par Ou Impar ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

numero = 0
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

par = 0
    # Nome Da Variável = par.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

impar = 0
    # Nome Da Variável = impar.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (numero != -999):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.
    
    numero = int(input("* Digite Um Número: "))
        # Nome Da Variável = numero.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    print ("=" * 60)

    if (numero != -999):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if (numero % 2 == 0):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        
            par = par + 1
                # Nome Da Variável = par.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> para + 1

        elif (numero % 2 == 1):
            # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            impar = impar + 1
                # Nome Da Variável = impar.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> impar + 1

print ("- Voçê Digitou {} Números Pares e {} Números Impares!!!".format(par, impar))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)


