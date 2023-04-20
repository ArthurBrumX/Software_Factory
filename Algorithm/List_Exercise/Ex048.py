# 48 - Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual condição de pagamento escolhidae efetuar o cálculo adequado.

# Código Condição de pagamento:

# 1 - À vista em dinheiro ou pix, recebe 10% de desconto;
# 2 - À vista no cartão de crédito,recebe 5% de desconto
# 3 - Em duas vezes, preço normal de etiqueta sem juros;
# 4 - Em três vezes, preço normal de etiqueta mais juros de 10%;

print ("=" * 60)

print ("*** I Love Coffee Roupas ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

preco_produto = int(input("* Digite o valor a ser pago pelo produto: "))
    # Nome Da Variável = preco_produto.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("[1] -- Dinheiro, Debito ou Pix")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("[2] -- Cartão De Crédito")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)

opcao = int(input("* Como voce deseja efetuar o pagamento: "))
    # Nome Da Variável = opcao.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

print ("=" * 60)

if (opcao == 1):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    desconto = preco_produto * 10 / 100
        # Nome Da Variável = desconto.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> preco_produto * 10 / 100

    novo_valor = preco_produto - desconto
        # Nome Da Variável = novo_valor.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> proco_produto - (Valor da Variável: ) -> desconto

    print ("- Voçê escolheu a Opcao (1) e recebeu o desconto de {}".format(desconto))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

    print ("- O Novo Valor a Ser Pago é De: R$ {}".format(novo_valor))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (opcao == 2):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    opcao_1 = input("* O Pagamento é AVISTA no Cartão de Credito [S/N]: ")
        # Nome Da Variável = opcao_1.
        # Tipo Da Variável = Str (String).
        # Função = Entrada De Dados.

    print ("=" * 60)

    if (opcao_1 == "Sim") or (opcao == "sim"):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        desconto = preco_produto * 5 / 100
            # Nome Da Variável = desconto.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> preco_produto * 5 / 100

        novo_valor = preco_produto - desconto
            # Nome Da Variável = soma.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> preco_produto - (Valor da Variável: ) -> desconto

        print ("- Voce escolheu a Opcao (2) a vista no cartão e recebeu o desconto de {}".format(desconto))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

        print ("- O Novo Valor a Ser Pago é De: R$ {}".format(novo_valor))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (opcao_1 == "Não") or (opcao_1 == "não") or (opcao_1 == "nao") or (opcao_1 == "Nao"):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        opcao_2 = int(input("Vai ser parcelado em quantas vezes: "))
            # Nome Da Variável = opcao_2.
            # Tipo Da Variável = Int (Inteiro).
            #Função = Entrada De Dados.


        print ("=" * 60)

        if (opcao_2 == 2):
            # If = Se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- Preço normal Da Etiqueta Sem juros!")
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.

            print ("- O Novo Valor a Ser Pago é De: R$ {}".format(preco_produto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

        elif (opcao_2 == 3):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            juros = preco_produto * 10 / 100
                # Nome Da Variável = juros.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> preco_produto * 10 / 100

            novo_valor = preco_produto + juros
                # Nome Da Variável = soma.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> preco_produto + (Valor da Variável: ) -> juros

            print ("- Preço normal Da Etiqueta mais juros de 10% de juros!")
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.

            print ("- O Novo Valor a Ser Pago é De: R$ {}".format(juros))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).


print ("=" * 60)







