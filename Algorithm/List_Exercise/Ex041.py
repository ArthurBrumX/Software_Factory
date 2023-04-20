# 41 - Três amigos, Joceyr, Thiago e Alexandre. decidiram rachar igualmente a conta de um bar. 
# Faça um algoritmopara ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que Joceyr e Thiago não paguem centavos. 
# Ex: uma conta de R$101,53 resulta em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53 para Alexandre.

print ("=" * 60)

print ("* Sejá Bem-Vindo!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

valor_conta = float(input("* Digite o Valor Total Da Conta: "))
    # Nome Da Variável = valor_conta.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

divisao = valor_conta / 3
    # Nome Da Variável = divisao.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> valor_conta  / 3

joceyr = round(divisao)
    # Nome Da Variável = joceyr.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

alexandre = round(divisao)
    # Nome Da Variável = alexandre.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

thiago = valor_conta -joceyr- alexandre
    # Nome Da Variável = thiago.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

print ("- O valor que Joceyr irá pagar é de: R$ {}".format(joceyr))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O valor que Alexandre irá pagar é de: R$ {}".format(alexandre))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print (f"- O valor que thiago irá {thiago}pagar é de: R$ {thiago:.2f}")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)

