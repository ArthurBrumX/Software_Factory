# 88 - Máquina de café

# Uma máquina de vender café funciona da seguinte forma: o usuário seleciona um tipo de café, insere algumas notas ou moedas na máquina e, se a quantia paga for suficiente 
# para pagar o café desejado, a máquina enche um copo descartável com o tipo de café selecionado e dá o troco em moedas. Faça um programa para imitar esse comportamento: o 
# usuário informa qual é o tipo de café desejado e o valor pago, e o seu programa deve dizer qual deve ser o valor do troco e quantas moedas são necessárias para pagar esse troco.
# Considere a existência de moedas com os seguintes valores: R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01.A tabela de preços é dada abaixo:

moeda = 1.0
    # Nome Da Variável = ced.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

tottroco = 0
    # Nome Da Variável = totced.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

cafe_normal = 1.05

cafe_expresso = 1.52

capuccino = 2.17

mocaccino = 2.36

troco = 0

print("=" * 60)

print ("Tipo De Café   |    Preço")

print ("Café Normal    |   R$1,05")
print ("Café Expresso  |   R$1,52")
print ("Capuccino      |   R$2.17")
print ("mocaccino      |   R$2,36")

print("=" * 60)

escolha = (input("* Qual tipo de Café Voce Vai querer: "))

if (escolha == "cafe normal" ):

    escolha = cafe_normal

    dinheiro = int(input("Digite a quantia de dinheiro entregue: "))

    print("=" * 60)

if (escolha == "cafe expresso" ):

    escolha = cafe_expresso

    dinheiro = int(input("Digite a quantia de dinheiro entregue: "))

    print("=" * 60)

if (escolha == "capuccino" ):

    escolha = capuccino

    dinheiro = int(input("Digite a quantia de dinheiro entregue: "))

    print("=" * 60)

if (escolha == "mocaccino" ):

    escolha = mocaccino

    dinheiro = int(input("Digite a quantia de dinheiro entregue: "))

    print("=" * 60)

troco = dinheiro - escolha

if troco > 0:

    print ("Valor do troco: R$ %s." % troco)

    print("")

total = troco

if total >= troco:
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    total -= troco
        # Nome Da Variável = total.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) ->  total - (Valor da Variável: ) ->  troco 

    tottroco += 1
        # Nome Da Variável = tottroco.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) ->  tottroco - 1


else:
    # Else = SeNão
        # Se Senhum for verdade, execute o codigo a baixo.

    if tottroco > 0:
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print (f"total De {tottroco} troco ulas De R$ {troco}")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).


    if troco == 1.0:
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        troco = 0.50
            # Nome Da Variável = troco.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

    elif troco == 0.50:
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        troco = 0.25
            # Nome Da Variável = troco.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

    elif troco == 0.25:
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        troco = 0.10
            # Nome Da Variável = troco.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

    elif troco == 0.10:
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        troco = 0.05
            # Nome Da Variável = troco.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

    elif troco == 0.05:
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        troco = 0.01
            # Nome Da Variável = troco.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

    tottroco = 0
        # Nome Da Variável = tottroco.
        # Tipo Da Variavel = Int (Inteiro).
        # Função = Atribuição De Valor.

    if total == 0:
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("=" * 60)

print ("Fim troco")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        
print ("=" * 60)


