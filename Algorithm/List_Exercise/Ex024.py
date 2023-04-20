# 24 - A lanchonete GostoSoft vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada 
# fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, 
# e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

print ("=" * 60)

print ("*** Lanchonete GostoSoft ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Mega Promoção De Sanduiches *")
    # Apresentação Ao Usuário.

print ("=" * 60)

pergunta = int(input("* Qual A Quantidade De Sanduiches Que Voçê Deseja: "))
    # Nome Da Variável = perguntas.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Entrada De Dados.

grama_pre = 50
    # Nome Da Variável = grama_pre.
    # Tipo Da Variavel = int (Inteiro).
    # Função = Atribuição De Valor.

grama_quei = 50
    # Nome Da Variável = grama_quei.
    # Tipo Da Variavel = int (Inteiro).
    # Função = Atribuição De Valor.

grama_hamb = 100
    # Nome Da Variável = grama_hamb.
    # Tipo Da Variavel = int (Inteiro).
    # Função = Atribuição De Valor.

conta = pergunta * grama_pre
    # Nome Da Variável = conta.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> pergunta * (Valor Da Variável: ) -> grama_pre

conta_1 = pergunta * grama_quei
    # Nome Da Variável = conta_1.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> pergunta * (Valor Da Variável: ) -> grama_quei

conta_2 = pergunta * grama_hamb
    # Nome Da Variável = conta_2.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> pergunta * (Valor Da Variável: ) -> grama_hamb

sanduiche = grama_pre + grama_quei + grama_hamb
    # Nome Da Variável = sanduiche.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> grama_pre + (Valor Da Variável: ) -> grama_quei + (Valor Da Variável: ) -> grama_hamb

peso = pergunta * sanduiche
    # Nome Da Variável = peso.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> pergunta * (Valor Da Variável: ) -> sanduiche

print ("=" * 60)

print ("- Para Fazer {} Sanduiches:".format(pergunta))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Voçê Precisa-rá De {} Gramas De Queijo!".format(conta_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Voçê Precisa-rá De {} Gramas De Presunto!".format(conta))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Voçê Precisa-rá De {} Gramas De Hamburger!".format(conta_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

if (peso <= 999):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- No Total Os Seus Sanduiches Vão Pesar {} Gramas!".format(peso))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).


elif(peso >999):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.


    print("No Total Os Seus Sanduiches Vão Pesar kg {}".format(peso))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60 ) 





