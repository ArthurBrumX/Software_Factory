# 73 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os 
# códigos utilizados são:

# 1 , 2, 3, 4 - Votos para os respectivos candidatos 

# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)

# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:

# • O total de votos para cada candidato;
# • O total de votos nulos;
# • O total de votos em branco;
# • A percentagem de votos nulos sobre o total de votos;
# • A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print ("=" * 60)

print ("*** Eleição Presidencial ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador = 0
    # Nome Da Variável = contatador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

jose = 0 
    # Nome Da Variável = jose.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

joao = 0
    # Nome Da Variável = joao.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

fernando = 0
    # Nome Da Variável = fernando.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

armando = 0
    # Nome Da Variável = armando.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

nulo = 0 
    # Nome Da Variável = nulo.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

branco = 0
    # Nome Da Variável = branco.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

voto = 0
    # Nome Da Variável = voto.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

print ("CANDIDATOS")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- [1] --- José ")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- [2] --- João")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- [3] --- Fernando")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- [4] --- Armando \n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- [5] --- NULO")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("- [6] --- BRANCO \n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)

while (contador < 10):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    voto = int(input("- Digite o Número Do Seu Candidato: "))  
        # Nome Da Variável = voto.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

    if (voto == 1):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        jose = jose + 1
            # Nome Da Variável = jose.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> jose + 1

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

    elif (voto == 2):
        # elIf = SeNão Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        joao = joao + 1
            # Nome Da Variável = joao.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> joao + 1

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

    elif (voto == 3):
        # elIf = SeNão Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        fernando = fernando + 1
            # Nome Da Variável = fernando.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> fernando + 1

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

    elif (voto == 4):
        # elIf = SeNão Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        armando = armando + 1
            # Nome Da Variável = armando.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> armando + 1

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

    elif (voto == 5):
        # elIf = SeNão Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        nulo = nulo + 1
            # Nome Da Variável = nulo.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> nulo + 1

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1

    elif (voto == 6):
        # elIf = SeNão Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

        branco = branco + 1
            # Nome Da Variável = branco.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> branco + 1

        contador = contador + 1
            # Nome Da Variável = contador.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> contador + 1
print ("=" * 60)


print ("- O Total De Votos Do Candidato Jose é De: {}".format(jose))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Total De Votos Do Candidato João é De: {}".format(joao))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Total De Votos Do Candidato Fernando é De: {}".format(fernando))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Total De Votos Do Candidato Armando é De: {} \n".format(armando))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- O Total De Votos Nulos é De: {}".format(nulo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O Total De Votos Brancos é De: {}".format(branco))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

porcent_nul = nulo * 10 / 100

porcent_total_vots = branco * 10 / 100

print ("A percentagem de votos nulos sobre o total de votos é {}".format(porcent_nul))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("A Porcentagem De Votos Em Brancos Sobre o total de Votos é: {}".format(porcent_total_vots))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)


