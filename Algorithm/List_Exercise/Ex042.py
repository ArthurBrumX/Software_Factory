# 42 - A fábrica de refrigerantes Gui-Cola vende seu produto em três formatos:
# Lata de 350 ml; Garrafa de 600 ml; Garrafa de 2 litros.
# Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

print ("=" * 60)

print ("*** Fábrica De Refrigerantes Gui-Cola ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)


ml_lata = 350
    # Nome Da Variável = ml_lata.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

ml_garrafa = 600
    # Nome Da Variável = ml_garrafa.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

l_garrafa_1 = 2000
    # Nome Da Variável = l_garrafa.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

quant_lata = float(input("* Quantas Lata de 350ml Vai Querer: "))
    # Nome Da Variável = quant_lata.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

quant_garrafa = float(input("* Quantas Garrafas De 600ml Vai Querer: "))
    # Nome Da Variável = quant_garrafa.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

quant_garrafa_1 = float(input("* Quantas Garrafas De 2 Litros Vai Querer: "))
    # Nome Da Variável = quant_garrafa_1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

litros_latas = quant_lata * ml_lata
    # Nome Da Variável = litros_latas.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> quant_lata * (Valor da Variável: ) -> ml_lata

litros_garrafa = quant_garrafa * ml_garrafa
    # Nome Da Variável = litros_garrafa.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> quant_garrafa * (Valor da Variável: ) -> ml_garrafa

litros_garrafa_1 = quant_garrafa_1 * l_garrafa_1
    # Nome Da Variável = litros_garrafa_1.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> quant_garrafa_1 * (Valor da Variável: ) -> l_garrafa_1
total_litros = litros_latas + litros_garrafa + litros_garrafa_1
    # Nome Da Variável = total_litros.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> litros_latas + (Valor da Variável: ) -> litros_garrafa + (Valor da Variável: ) -> litros_garrafa_1

print ("=" * 60)

print ("- O total De Litros vendidos é de: {}".format(total_litros))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)

