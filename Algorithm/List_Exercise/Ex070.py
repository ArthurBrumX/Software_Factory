# 70 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior
# resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as
# cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o
# melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da
# execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto: 6.5 m
# Pior salto: 5.3 m

print ("=" * 60)

print ("*** Competição De Salto Em Distância ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador = 0
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

melhor_salto = 0
    # Nome Da Variável = melhor_salto.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

pior_salto = 0
    # Nome Da Variável = pior_salto.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

nome = input("* Digte o Nome Do Atleta: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Atribuição De Valor.

if (nome == " "):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    nome = input("* Digte o Nome Do Atleta:")
        # Nome Da Variável = nome.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

print ("=" * 60)

while (contador != 1):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.
    
    primeiro = float(input("* Digite A Distancia Do Primeiro Salto: "))
        # Nome Da Variável = primeiro.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 1 ):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
       
       melhor_salto = primeiro
            # Nome Da Variável = melhor_salto.
            # Tipo Da Variavel = float (Real).
            # Função = Atribuição De Valor.

       pior_salto = primeiro
            # Nome Da Variável = pior_salto.
            # Tipo Da Variavel = float (Real).
            # Função = Atribuição De Valor.

    else:
        
        if primeiro > melhor_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_salto = primeiro
                # Nome Da Variável = melhor_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if primeiro < pior_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_salto = primeiro
                # Nome Da Variável = pior_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("O Primeiro Salto é De: {} m".format(primeiro))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 2):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    segundo = float(input("* Digite a Distancia Do Segundo Salto: "))
        # Nome Da Variável = segundo.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 2):
        # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if segundo > melhor_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_salto = segundo
                # Nome Da Variável = melhor_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if segundo < pior_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_salto = segundo
                # Nome Da Variável = pior_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.   

print ("O Segundo Salto é De: {} m".format(segundo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 3):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    terceiro = float(input("* Digite a Distancia Do Terceiro Salto: "))
        # Nome Da Variável = terceiro.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 3):
        # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if terceiro > melhor_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_salto = terceiro
                # Nome Da Variável = melhor_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.


        if terceiro < pior_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_salto = terceiro
                # Nome Da Variável = pior_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("O Terceiro Salto é De: {} m".format(terceiro))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 4):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    quarto = float(input("* Digite a Distancia Do Quarto Salto: "))
        # Nome Da Variável = quarto.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 4):
        # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if quarto > melhor_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_salto = quarto
                # Nome Da Variável = melhor_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if quarto < pior_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_salto = quarto
                # Nome Da Variável = pior_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("O Quarto Salto é De: {} m".format(quarto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 5):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    quinto = float(input("* Digite a Distancia Do Quinto Salto: "))
        # Nome Da Variável = quinto.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 5):
        # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if quinto > melhor_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_salto = quinto
                # Nome Da Variável = melhor_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if quinto < pior_salto:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_salto = quinto
                # Nome Da Variável = pior_salto.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

media = (primeiro + segundo + terceiro + quarto + quinto) - melhor_salto - pior_salto
    # Nome Da Variável = media.
    # Função = Calculo Com Variáveis
    # Calculo:(Valor da Variável)-> primeiro + (Valor da Variável)-> segundo + (Valor da Variável)-> terceiro + (Valor da Variável)-> quarto + (Valor da Variável)-> quinto
        # calculo: - (Valor da Variável)-> melhor_salto - (Valor da Variável)-> pior_salto

print ("O Quinto Salto é De: {} m".format(quinto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)


print ("Atleta: {} \n".format(nome))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("Primeiro Salto: {} m \n".format(primeiro))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("Segundo Salto: {} m \n".format(segundo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("Terceiro Salto: {} m \n".format(terceiro))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("Quarto Salto: {} m \n".format(quarto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("Quinto Salto: {} m \n".format(quinto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print("Melhor Salto: {} m \n".format(melhor_salto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("Pior Salto: {} m".format(pior_salto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)
               


