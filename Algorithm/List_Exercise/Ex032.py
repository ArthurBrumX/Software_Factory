# 32 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
# existentes na máquina.

# • Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1; 
# • Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print ("=" * 60)

print ("{:^30}".format("Banco Consumidor!!"))
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
print ("* Vamos Realizar Um Aaque *")
    # Apresentação Ao Usuário.

print ("=" * 60)

valor = int(input("Que Valor voce quer sacar: R$"))
    # Nome Da Variável = valor.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Entrada De Dados.

total = valor
    # Nome Da Variável = total.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

ced = 100
    # Nome Da Variável = ced.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

totced = 0
    # Nome Da Variável = totced.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while True:
    # While = Enquanto
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.   

    if total >= ced:
         # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

         total -= ced
            # Nome Da Variável = total.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) ->  total - (Valor da Variável: ) ->  ced 

         totced += 1
            # Nome Da Variável = totced.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) ->  totced - 1


    else:
        # Else = SeNão
            # Se Senhum for verdade, execute o codigo a baixo.

        if totced > 0:
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print (f"total De {totced} cedulas De R$ {ced}")
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).


        if ced == 100:
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            ced = 50
                # Nome Da Variável = ced.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        elif ced == 50:
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            ced = 10
                # Nome Da Variável = ced.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        elif ced == 10:
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            ced = 5
                # Nome Da Variável = ced.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        elif ced == 5:
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            ced = 1
                # Nome Da Variável = ced.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        totced = 0
            # Nome Da Variável = totced.
                # Tipo Da Variavel = Int (Inteiro).
                # Função = Atribuição De Valor.

        if total == 0:
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            break
                # Break = Pare

print ("=" * 60)

print ("Volte Sempre!!")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        
print ("=" * 60)