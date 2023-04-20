# 87 - Crie um algoritmo para uma empresa de transportes que, a partir do peso de uma encomenda fornecida pelo usuário, calcule o preço da remessa conforme aseguinte tabela:

print ("=" * 60)

print ("*** Transportadora Inozuki ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

peso = float(input("Digite o peso em grama Da Encomenda: "))

print ("=" * 60)


if (peso <= 500):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    valor = 1.10
        # Nome Da Variável = valor.
        # Tipo Da Variavel = Float (Real).
        # Função = Atribuição De Valor.


elif (peso > 500) and (peso < 2000):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    valor = 2.20
        # Nome Da Variável = valor.
        # Tipo Da Variavel = Float (Real)..
        # Função = Atribuição De Valor.

elif (peso >= 2000) and (peso <= 10000):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    valor = 3.70
        # Nome Da Variável = valor.
        # Tipo Da Variavel = Float (Real).
        # Função = Atribuição De Valor.

elif (peso > 10000) and (peso <= 10999):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    valor = 5
        # Nome Da Variável = valor.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (peso >= 1100):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    valor = 5 + 3.80
        # Nome Da Variável = valor.
        # Tipo Da Variavel = Float (Real).
        # Função = Atribuição De Valor.

print ("O valor Da Encomenda é de: R${}".format(valor))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)



