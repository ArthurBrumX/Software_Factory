# 72 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua 
# média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Aparecido Parente

# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:

print ("=" * 60)

print ("*** competição de ginástica ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador = 0
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

melhor_nota = 0
    # Nome Da Variável = melhor_nota.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

pior_nota = 0
    # Nome Da Variável = pior_nota.
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
    
    nota_1 = float(input("* Digite a Primeira Nota: "))
        # Nome Da Variável = nota_1.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 1 ):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
       
       melhor_nota = nota_1
            # Nome Da Variável = melho_nota.
            # Tipo Da Variavel = float (Real).
            # Função = Atribuição De Valor.

       pior_nota = nota_1
            # Nome Da Variável = pior_nota.
            # Tipo Da Variavel = float (Real).
            # Função = Atribuição De Valor.

    else:
        
        if nota_1 > melhor_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_nota = nota_1
                # Nome Da Variável = melhor_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if nota_1 < pior_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_nota = nota_1
                # Nome Da Variável = pior_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("- A Primeira nota é: {}".format(nota_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 2):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    nota_2 = float(input("* Digite a Segunda Nota: "))
        # Nome Da Variável = nota_2.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 2):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if nota_2 > melhor_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_nota = nota_2
                # Nome Da Variável = melhor_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if nota_2 < pior_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_nota = nota_2
                # Nome Da Variável = pior_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.   

print ("- A Segunda Nota é: {}".format(nota_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 3):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    nota_3 = float(input("* Digite a Terceira Nota: "))
        # Nome Da Variável = nota_3.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 3):
        # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if nota_3 > melhor_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_nota = nota_3
                # Nome Da Variável = melhor_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.


        if nota_3 < pior_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_nota = nota_3
                # Nome Da Variável = pior_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("- A Terceira Nota é: {}".format(nota_3))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 4):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    nota_4 = float(input("* Digite a Quarta Nota: "))
        # Nome Da Variável = nota_4.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 4):
        # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if nota_4 > melhor_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_nota = nota_4
                # Nome Da Variável = melhor_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if nota_4 < pior_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_nota = nota_4
                # Nome Da Variável = pior_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("- A Quarta Nota é: {}".format(nota_4))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 5):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    nota_5 = float(input("* Digite a Quinta Nota: "))
        # Nome Da Variável = nota_5.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 5):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if nota_5 > melhor_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_nota = nota_5
                # Nome Da Variável = melhor_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if nota_5 < pior_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_nota = nota_5
                # Nome Da Variável = nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("A Quinta Nota é: {}".format(nota_5))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 6):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

        nota_6 = float(input("* Digite a Sexta Nota: "))
            # Nome Da Variável = nota_6.
            # Tipo Da Variável = float (Real).
            # Função = Entrada De Dados.

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

        if (contador == 6):
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            if nota_6 > melhor_nota:
                # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

                melhor_nota = nota_6
                    # Nome Da Variável = melhor_nota.
                    # Tipo Da Variavel = float (Real).
                    # Função = Atribuição De Valor.

            if nota_6 < pior_nota:
                # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

                pior_nota = nota_6
                    # Nome Da Variável = pior_nota.
                    # Tipo Da Variavel = float (Real).
                    # Função = Atribuição De Valor.
            
print ("A Sexta Nota é: {}".format(nota_6))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

while (contador != 7):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    nota_7 = float(input("* Digite a Setima Nota: "))
        # Nome Da Variável = nota_6.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    if (contador == 7):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        if nota_7 > melhor_nota:
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            melhor_nota = nota_7
                # Nome Da Variável = melhor_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

        if nota_7 < pior_nota:
                # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            pior_nota = nota_7
                # Nome Da Variável = pior_nota.
                # Tipo Da Variavel = float (Real).
                # Função = Atribuição De Valor.

print ("A Setima Nota é: {}".format(nota_7))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

adicao = nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6 + nota_7
    # Nome Da Variável = dicao.
    # Função = Calculo Com Variáveis
    # Calculo:(Valor da Variável)-> nota_1 + (Valor da Variável)-> nota_2 + (Valor da Variável)-> nota_3 + (Valor da Variável)-> nota_4 + (Valor da Variável)-> nota_5
        # Calculo + (Valor da Variável)-> nota_6 + (Valor da Variável)-> nota_7

subtracao = adicao - melhor_nota - pior_nota
    # Nome Da Variável = subtracao.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) ->adicao - (Valor da Variável: ) -> melhor_nota - (Valor da Variável: ) -> pior_nota

media = subtracao / 5
    # Nome Da Variável = media.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> subtracao / 5

print ("=" * 60)


print ("- Atleta: {} \n".format(nome))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("- Nota: {} \n".format(nota_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Nota: {} \n".format(nota_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Nota: {} \n".format(nota_3))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Nota: {} \n".format(nota_4))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Nota: {} \n".format(nota_5))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Nota: {} \n".format(nota_6))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Nota: {} \n".format(nota_7))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)

print("- Resultado Final: {} \n".format(media))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("- Melhor Nota: {} \n".format(melhor_nota))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print("- Pior Nota: {}".format(pior_nota))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)



