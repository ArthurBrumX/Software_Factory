# 58- Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. 
# Ex: Bife acebolado R$15,00; Lasanha R$25,00).

# A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário, “Aceita pagar a gorjeta do garçom 10% sobre o 
#valor do prato”. Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso contrário, mostrar o valor final (somente o valor do prato).

print ("=" * 60)

print ("*** Restaurante Miojo De Carne ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

print (" *** Cardapio! **")
    # Apresentação Ao Usuário.

print ("=" * 60)

print ("[1] ---> Bife Acebolado.......R$ 15.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[2] ---> Lasanha..............R$ 25.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[3] ---> Frango Empanado......R$ 10.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[4] ---> Frango Frito.........R$ 20.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[5] ---> Macarrão c/ Carne....R$ 12.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[6] ---> Feijoada.............R$ 30.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[7] ---> Strogonoff...........R$ 17.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[8] ---> Escondidinho.........R$ 11.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[9] ---> Frango Assado........R$ 18.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[10] ---> Carne d/ Panela.....R$ 12.00")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

Bife_Acebolado = 15
    # Nome Da Variável = Bife_Acebolado.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Lasanha = 25
    # Nome Da Variável = Lasanha.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Frango_Empanado = 10
    # Nome Da Variável = Frango_Empanado.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Frango_Frito = 20
    # Nome Da Variável = Frango_Frito.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Macarrão_com_Carne = 12
    # Nome Da Variável = acarrão_com_Carne.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Feijoada = 30
    # Nome Da Variável = Feijoada.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Strogonoff = 17
    # Nome Da Variável = Strogonoff.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Escondidinho = 11
    # Nome Da Variável = Escondidinho.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Frango_Assado = 18
    # Nome Da Variável = Frango_Assado.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

Carne_de_Panela = 12
    # Nome Da Variável = Carne_de_Panela.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

print ("=" * 60)

escolha = float(input("* Qual Número Do Prato voce deseja escolhe: "))
    # Nome Da Variável = escolha.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

if (escolha == 1):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Bife Acebolado ")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Bife_Acebolado
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.


elif (escolha == 2):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Lasanha")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Lasanha
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 3):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Frango Empanado")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Frango_Empanado
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 4):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Frango Frito")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Frango_Frito
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 5):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Macarrão c/ Carne")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Macarrão_com_Carne
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 6):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Feijoada")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Feijoada
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 7):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Strogonoff")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Strogonoff
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 8):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Escondidinho")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Escondidinho
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 9):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Frango Assado")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Frango_Assado
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

elif (escolha == 10):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Voçê Escolheu: Carne d/ Panela")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    opcao = Carne_de_Panela
        # Nome Da Variável = opcao.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

print ("=" * 60)

gorjeta = input("* Aceita pagar a gorjeta do garçom 10% sobre o valor do prato [S/N]: ")
    # Nome Da Variável = gorjeta.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

if (gorjeta == "Sim") or (gorjeta == "sim"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    op_gorjerta = opcao * 10 / 100
        # Nome Da Variável = op_gorjerta.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> opcao * 10 / 100

    valor_total = opcao + op_gorjerta
        # Nome Da Variável = valor_total.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> opcao + (Valor da Variável: ) -> op_gorjerta

    print ("- O Valor Da Conta é De: R$ {}".format(valor_total))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (gorjeta == "Não") or (gorjeta == "não") or (gorjeta == "nao") or (gorjeta == "Nao"):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Valor Da Conta é De: R$ {}".format(opcao))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)