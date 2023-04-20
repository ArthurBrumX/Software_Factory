# 14 - Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcule e escreva o saldo atual (saldo atual = saldo - débito + crédito). 
# Também teste se saldo atual for maior ou igual a zero. Em seguida escreva a mensagem 'Saldo Positivo', senão, escrever a mensagem 'Saldo Negativo' .

print ("=" * 60)

print ("*** Banco Arthur Passou No Curso ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Olá Cliente! Digite Algumas Informações Para Prosseguirmos! *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

nome = input("* Digite Seu Nome Completo: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.


numero = float(input("* Digite o número da conta: "))
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

print ("-" * 60)

saldo = float(input("* Digite Seu Saldo Bancario Atual: "))
    # Nome Da Variável = saldo.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

print ("-" * 60)

debito = float(input("* Digite o Valor Da Sua Divida Bancaria Em Aberto: "))
    # Nome Da Variável = debito.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

print ("-" * 60)

credito = float(input("* Digite Seu Crédito Bancario Disponivel: "))
    # Nome Da Variável = credito.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

print ("-" * 60)

saldo_atual = saldo - debito + credito
    # Nome Da Variável = saldo_atual.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> saldo - (Valor Da Variável: ) -> debito + (Valor Da Variável: ) -> Credito

print ("-" * 60)

if (saldo_atual >= 0):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("Senhor {} O seu saldo é de R${}!".format(nome, saldo_atual))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("O Seu Saldo Bancario Esta Positivo!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (saldo_atual <= -1):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("Senhor {} O Seu Saldo é De R${}!!".format(nome, saldo_atual))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("O Seu Saldo Esta Negativo!!!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)

print ("*** Fim Da Consulta! Volte Sempre!!! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)