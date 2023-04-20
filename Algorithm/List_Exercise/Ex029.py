# 29 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# • Para homens: (72.7*h) - 58

# • Para mulheres: (62.1*h) - 44.7

print ("=" * 60)

print ("*** Calculo De IMC ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Vamos Descobrir Qual Seu IMC!! *")
print ("* Preencha Os Dados a Baixo: ")
    # Apresentação Ao Usuário.

print ("=" * 60)

nome = input("* Digite Seu Nome Completo: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados

sexo = input("* Digite Seu Sexo [M/F]: ")
    # Nome Da Variável = sexo.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

altura = float(input("* Digite Sua altura: "))
    # Nome Da Variável = altura.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

if (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
    
    imc_masc = (72.7 * altura) - 58
        # Nome Da Variável = imc_masc.
        # Função = Calculo Com Variáveis
        # Calculo: 72.7 * (Valor da Variável: ) -> altura - 58

    print ("=" * 60)

    print ("- {} O Seu IMC Masculino Ideal Será De: {}KG!".format(nome, imc_masc))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    imc_fem = (62.1 * altura) - 44.7
        # Nome Da Variável = imc_fem.
        # Função = Calculo Com Variáveis
        # Calculo: 62.1 * (Valor da Variável: ) -> altura - 44.7

    print ("=" * 60)

    print ("- {} O Seu IMC Feminino Ideal Será De: {}KG!".format(nome, imc_fem))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).


print ("=" * 60)

print ("*** Fim Do Calculo!!! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)