# 39 - Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. 
# Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.

print ("=" * 60)

print ("*** Restaurante a Quilo Sabor ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

dia = int(input("Digite o dia atual: "))
    # Nome Da Variável = venda_1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

mes = int(input("Digite o mes atual: "))
    # Nome Da Variável = venda_1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

dia_atual = 365 - dia
    # Nome Da Variável = dias_atuais.
    # Função = Calculo Com Variáveis
    # Calculo: 365 - (Valor da Variável: ) -> dia

mes_atual = 12 - mes
    # Nome Da Variável = mes_atual.
    # Função = Calculo Com Variáveis
    # Calculo: 12 - (Valor da Variável: ) -> mes

print ("Ja se passaram {} dias desde o comeco do ano ".format(dia_atual))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("Ja se passaram {} meses desde o comeco do ano ".format(mes_atual))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)

