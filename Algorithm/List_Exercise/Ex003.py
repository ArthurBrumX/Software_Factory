# 3 - Faça um algoritmo que leia o nome, o título eleitoral e o numero do candidato. Posteriormente imprima o resultado de cada variável linha abaixo de linha.

print ("=" * 60)

print ("*** Cabine Eleitoral ***")
    # Apresentação Ao Usuário.

print ("-" * 60)

print ("* Seja Bem Vindo Cidadão! ")
print ("* Insira Seus Dados Para Prosseguirmos!")
    # Apresentação Ao Usuário.

print ("=" * 60)

nome = input("-Digite Seu Nome Completo: ")
    # Nome Da Variável = nome.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

titulo = float(input("-Digite Seu Ttitulo De Eleitor Completo: "))
    # Nome Da Variável = titulo.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

numero_candidato = float(input("-Digite o Seu Numero De Candidatura: "))
    # Nome Da Variável = numero_candidato.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("* Nome Completo: {}".format(nome))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("* Titulo Eleitoral: N°{}".format(titulo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("* Numero Do Candidato: N°{}".format(numero_candidato))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("-" * 60)

print ("*** Dados Confirmados Com Sucesso! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)
