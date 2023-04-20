# 2 - Faça um algoritmo que leia o nome e as notas dos 4 bimestres de um aluno. Posteriormente imprima o resultado de cada variável linha abaixo de linha.

print ("=" * 60)

print ("*** Escola Tarda Mais Não Falha ***")
print ("*** Relatório De Notas Bimestrais! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

nome_aluno = input("-Digite o Nome Completo Do Aluno: ")
    # Nome Da Variável = nome_aluno.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("*** Aluno: ({}) ***".format(nome_aluno))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)

print ("-" * 60)

nota_primeiro = float(input("-Digite a Nota Do 1° Bimestre: "))
    # Nome Da Variável = nota_primeiro.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

nota_segundo = float(input("-Digite a Nota Do 2° Bimestre: "))
    # Nome Da Variável = nota_segundo.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

nota_terceiro = float(input("-Digite a Nota Do 3° Bimestre: "))
    # Nome Da Variável = nota_terceiro.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

nota_quarto = float(input("-Digite a Nota Do 4° Bimestre: "))
    # Nome Da Variável = nota_quarto.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("* Aluno ({})".format(nome_aluno))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)


print ("* Nota 1° Bimestre: {}".format(nota_primeiro))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)

print ("* Nota 2° Bimestre: {}".format(nota_segundo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)

print ("* Nota 3° Bimestre: {}".format(nota_terceiro))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)


print ("* Nota 4° Bimestre: {}".format(nota_quarto))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = formata o texto, alocando o valor de uma varivel no espaço: {}
        # Ex: .format(Nome_da_Variavel)

print ("-" * 60)

print ("*** Relatório Finalizado Com Sucesso! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)
