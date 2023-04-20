# 5 - Faça um algoritmo que leia o nome do aluno, o nome da disciplina, notas de 3 provas e calcule a média desse aluno. Posteriormente imprima o resultado de cada variável
# linha abaixo de linha.

print ("=" * 60)

print ("*** Escola Enilda Melhor Professora ***")
print ("* Seja Bem-Vindo(a) Professor(a)! *")
    # Apresentação Ao Usuário.

print ("=" * 60)

print ("* Relatório De Notas Bimestrais *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

nome = input("-Digite o Nome Do Aluno: ")
    # Nome Da Variável = nome.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.


nome_disciplina = input("-Digite o Nome Da Disciplina: ")
    # Nome Da Variável = nome_disciplina.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("* Aluno: {}".format(nome))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("* Disciplina: {}".format(nome_disciplina))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("¨" * 60)

primeira_nota = float(input("-Digite a Primeira Nota: "))
    # Nome Da Variável = primeira_nota.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

segunda_nota = float(input("-Digite a Segunda Nota: "))
    # Nome Da Variável = segunda_nota.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

terceira_nota = float(input("-Digite a Terceira Nota: "))
    # Nome Da Variável = terceira_nota.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.


media = primeira_nota + segunda_nota + terceira_nota / 3
    # Nome Da Variável = media.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> primeira_nota + (Valor Da Variável: ) -> segunda_nota + (Valor Da Variável: ) -> terceira_nota / (Dividido Por: ) -> 3

print ("-" * 60)

print ("* As Notas De ({}) foram: ".format(nome))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ()

print ("* 1° Bimestre: {}".format(primeira_nota))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("* 2° Bimestre: {}".format(segunda_nota))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("* 3° Bimestre: {}".format(terceira_nota))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("-" * 60)

print ("Sua Média Bimestral é: {}".format(media))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("*** Relatório Atualizado com Sucesso! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)