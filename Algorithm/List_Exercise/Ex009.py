# 9 - Faça um algoritmo que leia o nome de um aluno, o nome da disciplina, nota de 3 provas e calcule a média desse aluno e verifique se o aluno foi aprovado. Sabendo que para ser 
# aprovado a média deverá ser maior ou igual a 6,0.Posteriormente imprima o resultado de cada variável linha abaixo de linha.

print ("=" * 60)

print ("*** Escola Enilda Melhor Professora ***")
print ("* Seja Bem-Vindo(a) Professor(a)! *")
    # Apresentação Ao Usuário.

print ("=" * 60)


print ("* Relatório De Notas Bimestrais *")
    # Apresentação Ao Usuário.

print ("¨" * 60)


nome_aluno = input("-Digite o Nome Do Aluno: ")
    # Nome Da Variável = nome_aluno.
    # Tipo Da Variavel = Str (string).
    # Função = Entrada De Dados.

disciplina = input("-Digite o Nome Da Disciplina: ")
    # Nome Da Variável = disciplina.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("* Aluno: {}".format(nome_aluno))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("* Disciplina: {}".format(disciplina))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("¨" * 60)

nota_1 = float(input("* Digite a Primeira Nota: "))
    # Nome Da Variável = nota_1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

nota_2 = float(input("* Digite a Segunda Nota: "))
    # Nome Da Variável = nota_2.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

nota_3 = float(input("* Digite a Terceira Nota: "))
    # Nome Da Variável = nota_3
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

media_aluno = (nota_1 + nota_2 + nota_3) / 3
    # Nome Da Variável = media_aluno.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> primeira_nota + (Valor Da Variável: ) -> segunda_nota + (Valor Da Variável: ) -> terceira_nota / (Dividido Por: ) -> 3

print ("-" * 60)

print ("* As Notas De ({}) foram: ".format(nome_aluno))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print(" ")

print ("* 1° Bimestre: {}".format(nota_1))
    # Função = Entrada De Dados.
    # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("* 1° Bimestre: {}".format(nota_2))
    # Função = Entrada De Dados.
    # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("* 1° Bimestre: {}".format(nota_3))
    # Função = Entrada De Dados.
    # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

if (media_aluno >= 6):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-Sua Média Bimestral é: {}".format(media_aluno))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

    print ("** Aluno Aprovado! **")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

else:
    print ("-Sua Média Bimestral é: {}".format(media_aluno))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

    print ("** aluno reprovado! **")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)
    

print ("*** Relatório Atualizado com Sucesso! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)

