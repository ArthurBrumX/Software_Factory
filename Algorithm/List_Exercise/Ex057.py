# 57- O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada bimestre.
# Os pontos são atribuídos da seguinte forma:

# •Se um cliente comprar 0 livros, ele ganhará 0 pontos.
# •Se um cliente comprar um livro, ele ganhará 5 pontos.
# •Se um cliente comprar dois livros, ele ganhará 15 pontos.
# •Se um cliente comprar 3 livros, ele ganhará 30 pontos.
# •Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.

# Lista de brindes:

# De 20 à 30 pontos o cliente poderáescolher entre: Uma EcoBag OU Caneta personalizada
# De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.
# Acima de 65 o cliente poderáescolherentre: 2 livros (com valor máximo de R$100,00)OU Powerbank

print ("=" * 60)

print ("*** Livraria New York ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

livros_compr_1 = int(input("* Quantos livros foram comprados no 1° Mês: "))
    # Nome Da Variável = livros_compr_1.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

livros_compr_2= int(input("* Quantos livros foram comprados no 2° Mês: "))
    # Nome Da Variável = livros_compr_1.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

print ("=" * 60)

pontos = 0
    # Nome Da Variável = pontos.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

total_bimestre = livros_compr_1 + livros_compr_2
    # Nome Da Variável = total_bimestre.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) ->livros_compr_1 + (Valor da Variável: ) ->livros_compr_2

if (total_bimestre == 0):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    pontos = pontos + 0
        # Nome Da Variável = pontos.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    print ("- O Total De Pontos é: 0")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("- Com o Total De Pontos Não è Possivel Escolher Nenhum Brinde!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

elif (total_bimestre == 1):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    pontos = pontos + 1
        # Nome Da Variável = pontos.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    print ("- O Total De Pontos é: 1")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("- Com o Total De Pontos Não è Possivel Escolher Nenhum Brinde!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

elif (total_bimestre == 2):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    pontos = pontos + 2
        # Nome Da Variável = pontos.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    print ("- O Total De Pontos é: 15")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("- Com o Total De Pontos Não è Possivel Escolher Nenhum Brinde!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

elif (total_bimestre == 3):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    pontos = pontos + 30
        # Nome Da Variável = pontos.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    print ("** O Total De Pontos é: 30")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("** Premios Disponiveis **")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

    print ("[1] ---> Eco Bag")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("[2] ---> Caneta Personalizada")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

    escolha = int(input("* Qual Brinde Vai Querer: "))
        # Nome Da Variável = escolha.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    print ("=" * 60)

    if (escolha == 1):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens Voçê Escolheu: Uma Eco Bag!!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    elif (escolha == 2):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: Uma Caneta Personalizada!!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    print ("=" * 60)

elif (total_bimestre == 4):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    pontos = pontos + 60
        # Nome Da Variável = pontos.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    print ("- O Total De Pontos é: 60")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("** Premios Disponiveis **")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

    print ("[1] ---> 1-livro (Com Valor Máximo De R$ 30,00)")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("[2] ---> Luminária De Cabeceira ")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

    escolha = int(input("* Qual Brinde Vai Querer: "))
        # Nome Da Variável = escolha.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    if (escolha == 1):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: 1-livro !!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    elif (escolha == 2):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: Luminária De Cabeceira !!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    print ("=" * 60)

elif (total_bimestre > 4):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        
    ponto = pontos + 70
        # Nome Da Variável = pontos.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    print ("- O Total De Pontos é: 70")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("** Premios Disponiveis **")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

    print ("[1] ---> 1-livro (Com Valor Máximo De R$ 30,00)")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("[2] ---> Luminária De Cabeceira ")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("[3] ---> 2-Livros (Com Valor Máximo De R$ 100,00)")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("[4] ---> Power Bank")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

    escolha = int(input("* Qual Brinde Vai Querer: "))
        # Nome Da Variável = escolha.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

    if (escolha == 1):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: 1-livro !!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    elif (escolha == 2):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: Luminária De Cabeceira !!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    elif (escolha == 3):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: 2-Livros !!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    elif (escolha == 4):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Parabens voçê Escolheu: Power Bank !!")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    print ("=" * 60)
