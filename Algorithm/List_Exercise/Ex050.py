# 50- Construir um programa que leia um valor numérico inteiro e apresente como resultado os seus valores:

# sucessore antecessor.

print ("=" * 60)

print ("*** Sucessore Antecessor ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

numero = int(input("Digite Um Número: "))
    # Nome Da Variável = numero.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

antecessor = numero - 1
    # Nome Da Variável = antecessor.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> numero -1

sucessor = numero + 1
    # Nome Da Variável = sucessor.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> numero + 1

print ("O antecessor de {} será: {}!".format(numero, antecessor))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("O sucessor de {} será: {}!".format(numero, sucessor))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
         # Ex: .format(Nome_da_Variável).

print ("=" * 60)














