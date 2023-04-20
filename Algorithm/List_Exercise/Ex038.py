# 38 - O restaurante a quilo Sabor em Quilo cobra R$59,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) 
# e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

print ("=" * 60)

print ("*** Restaurante a Quilo Sabor ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

peso_prato = float(input("* KG do prato: "))   
    # Nome Da Variável = venda_2.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

peso_KG = 59
    # Nome Da Variável = peso_KG.
    # Tipo Da Variavel = int (Inteiro).
    # Função = Atribuição De Valor.

valor_total_prato = peso_prato * peso_KG
    # Nome Da Variável = valor_total_prato.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> peso_prato * (Valor da Variável: ) -> peso_KG

print ("- O valor a ser pago pelo prato feito é de: R$ {}".format(valor_total_prato))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)
