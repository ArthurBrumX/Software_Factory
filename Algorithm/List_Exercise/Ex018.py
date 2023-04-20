# 18 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
#menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.Desconto do IR:

    # Salário Bruto até 900 (inclusive) - isento
    # Salário Bruto até 1500 (inclusive) - desconto de 5%
    # Salário Bruto até 2500 (inclusive) - desconto de 10%
    # Salário Bruto acima de 2500 - desconto de 20% 

        # Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            # Salário Bruto: (5 * 220) : R$ 1100,00
            # (-) IR (5%) : R$ 55,00 
            # (-) INSS ( 10%) : R$ 110,00
            # FGTS (11%) : R$ 121,00
            # otal de descontos : R$ 165,00
            # Salário Liquido : R$ 935,00

print ("=" * 60)

print ("*** Empresa Codar Is My Life ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Consulta De Folha De Pagamento! *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

nome = input("* Digite o Nome Do Funcionario: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Srt (String).
    # Função = Entrada De Dados.

hora_trab = float(input("* Quanta Horas Por Mês ({}) Trabalha: ".format(nome)))
    # Nome Da Variável = hora_trab.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

valor_hora_trab = float(input("* Qual o Valor Da Hora Trabalhada De ({}): ".format(nome)))
    # Nome Da Variável = valor_hora_trab.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

Salário_bruto = valor_hora_trab * hora_trab
    # Nome Da Variável = salario_bruto.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> valor_hora_trab * (Valor da Variável: ) -> hora_trab

sindicato = (Salário_bruto * 3) / 100
    # Nome Da Variável = sindicato.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> Salário_bruto * 3 (Dividido Por: ) -> 100

FGTS = (Salário_bruto * 11) / 100
    # Nome Da Variável = FGTS.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> Salário_bruto * 11 (Dividido Por: ) -> 100

# Salário_liquido = Salário_bruto - sindicato - FGTS

if (Salário_bruto <= 900):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print("- O Funcionario ({}) Está Isento!".format(nome))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (Salário_bruto > 900) or (Salário_bruto <= 1500):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    descont_IR = Salário_bruto * 5 / 100
        # Nome Da Variável = desconto_IR.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario_bruto * 5 / (Dividido Por: ) -> 100

    Salário_liquido = Salário_bruto - sindicato - descont_IR - FGTS
        # Nome Da Variável = salario_liquido.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario_bruto - (Valor da Variável: ) -> sindicato - (Valor da Variável: ) -> desconto_IR - (Valor da Variável: ) -> FGTS

    print ("- O Salário liquido de ({}) será de R${} ".format(nome, Salário_liquido))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (Salário_bruto > 1500) or (Salário_bruto <= 2500):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    descont_IR = Salário_bruto * 10 / 100
        # Nome Da Variável = desconto_IR.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario_bruto * 10 / (Dividido Por: ) -> 100

    Salário_liquido = Salário_bruto - sindicato - descont_IR - FGTS
        # Nome Da Variável = salario_liquido.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario_bruto - (Valor da Variável: ) -> sindicato - (Valor da Variável: ) -> desconto_IR - (Valor da Variável: ) -> FGTS

    print ("- O Salário liquido De ({}) será de R${} ".format(nome, Salário_liquido))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (Salário_bruto > 2500):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    desconto_IR = Salário_bruto * 20 /100
        # Nome Da Variável = desconto_IR.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario_bruto * 20 / (Dividido Por: ) -> 100

    Salário_liquido = Salário_bruto - sindicato - desconto_IR - FGTS
        # Nome Da Variável = salario_liquido.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario_bruto - (Valor da Variável: ) -> sindicato - (Valor da Variável: ) -> desconto_IR - (Valor da Variável: ) -> FGTS

    print ("- O Salário liquido De ({}) será de R${} ".format(nome, Salário_liquido))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).


print ("=" * 60)