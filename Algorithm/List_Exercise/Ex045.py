# 45 - Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 

# a) a idade dessa pessoa em anos; 
# b) a idade dessa pessoa em meses; 
# c) a idade dessa pessoa em dias;
# d) a idade desss pessoa em semanas;

# dessa pessoa em semanas.

print ("=" * 60)

print ("* Sejá Bem-Vindo ")
    # Apresentação Ao Usuário.

print ("=" * 60)

ano_nasc = int(input("* Em Quem Ano Voce Nasceu: "))
    # Nome Da Variável = valor_conta.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

ano_atual = int(input("* Em Que Ano Nós Estamos: "))
    # Nome Da Variável = valor_conta.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

idade = ano_atual - ano_nasc
    # Nome Da Variável = idade.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> ano_atual - (Valor da Variável: ) -> ano_nasc

mes = idade * 12
    # Nome Da Variável = mes.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> idade * 12

semanas = idade * 52
    # Nome Da Variável = semanas.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> idade * 52

dias = idade * 365
    # Nome Da Variável = dia.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> idade * 365

print ("- Voce tem {} anos".format(idade))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Voce tem {} meses de vida".format(mes))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Voce tem {} dias de Vida".format(dias))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- voce tem {} semanas de vida".format(semanas))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)








