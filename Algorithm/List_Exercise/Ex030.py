# 30 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa 
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e navariável multa o valor da multa que 
# João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print ("=" * 60)

print ("*** Regulamento De Pesca Do Estado De São Paulo!! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Controle Excedente De Carga! *")
    # Apresentação Ao Usuário.

print ("=" * 60)

print ("*** Bem-Vindo João! ***")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

peso = float(input("* Digite o Peso Da Carga Total Dos Peixes: "))
    # Nome Da Variável = peso.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

if (peso > 50):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    excesso = peso - 50
        # Nome Da Variável = excesso.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> peso - 50

    multa = excesso * 4
        # Nome Da Variável = multa.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> excecssi * 4

    print ("=" * 60)

    print ("- O Peso Excedido Foi De: {} KG!! ".format(excesso))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).


    print ("- A Multa Refetente Ao Excesso De Peso Será De R$ {} Reais!!".format(multa))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).


elif (peso <= 50):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("=" * 60)


    print ("- João, Voçê Está livre de multas Referente a Está Carga! \n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("***Prossiga Com a Viagem Até a Proxima!!! ***")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.


print ("=" * 60)









