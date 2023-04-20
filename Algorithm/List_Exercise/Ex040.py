# 40 - João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. 
# Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um algoritmo que calcule e mostre quanto restará do salário do João

print ("=" * 60)

print ("* Sejá Bem-Vindo Joao!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

salario = 1200
    # Nome Da Variável = salario.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

conta_1 = 200
    # Nome Da Variável = conta_1.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

conta_2 = 120
    # Nome Da Variável = conta_2.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

val_juros_1 = conta_1 * 2 / 100
    # Nome Da Variável = val_juros_1.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> conta_1 * 2 / 100

val_juros_2 = conta_2 * 2 /100
    # Nome Da Variável = val_juros_2.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> conta_2  * 2 / 100

total_conta_1 = conta_1 + val_juros_1
    # Nome Da Variável = total_conta_1.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> conta_1  + (Valor da Variável: ) -> val_juros_1

total_conta_2 = conta_2 + val_juros_2
    # Nome Da Variável = total_conta_2.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> conta_2  + (Valor da Variável: ) -> val_juros_2

total_das_contas = total_conta_1 + total_conta_2
    # Nome Da Variável = total_das_contas.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> total_conta_1  + (Valor da Variável: ) -> total_conta_2

resto_salario = salario - total_conta_1 - total_conta_2
    # Nome Da Variável = resto_salario.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> salario  - (Valor da Variável: ) -> total_conta_1 - (Valor da Variável: ) -> total_conta_2

print ("- O valor da primeira conta com juros é de: R$ {}".format(total_conta_1))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O valor da segunda conta com jutos é de: R$ {}".format(total_conta_2))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Ambas as contas juntas e com juros ficou no valor de: {}".format(total_das_contas))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- Após o pagamento das contas joao ficou com: R$ {}".format(resto_salario))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)