# 19 - Faça um Programa que peça os 3 lados de um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

print ("=" * 60)

print ("*** Triangulos ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Descubra Qual Triangulo Forma! *")
    # Apresentação Ao Usuário.

print ("¨" * 60)


lado_1 = float(input("* Digite o primeiro lado do triangulo: "))
    # Nome Da Variável = lado_1.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

lado_2 = float(input("* Digite o segunfo lado do triangulo: "))
    # Nome Da Variável = lado_2.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

lado_3 = float(input("* Digite o terceiro lado do triangulo: "))
    # Nome Da Variável = lado_3.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

if (lado_1 == lado_2) and (lado_2 == lado_3):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print("- Formou Um Triângulo Equilátero!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).
        # Um triangulo equilátero é formado por tres lados iguais.

elif (lado_1 == lado_2) and (lado_2 == lado_1) and (lado_3 != lado_1 and lado_2):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print("- Formou Um Triangulo Isósceles!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).
        # Um triangulo Isósceles é formado por apenas 2 lados iguais e o terceiro lado diferente.

elif (lado_1 != lado_2) and (lado_2 != lado_3):
    # Elif = SeNão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print("- Formou Um Triangulo Escaleno!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).
        # Um triangulo Escaleno é formado por todos os lados deferente um do outro.


print ("=" * 60)