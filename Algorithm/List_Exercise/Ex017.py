# 17 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhes contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e reajuste-o seguindo o seguinte critério baseado no salário atual:

    # salários até R$ 280,00 (incluindo) : aumento de 20%
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

        # o salário antes do reajuste;
        # o percentual de aumento aplicado;
        # o valor do aumento;
        # o novo salário, após o aumento;

print ("=" * 60)

print ("*** Organizações Tabajara ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("*** Reajuste salárial ***")
    # Apresentação Ao Usuário.

print ("-" * 60)

nome = input("* Digite o nome do funcionario: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

salario = float(input("* Digite o Salario do funcionario ({}): ".format(nome)))
    # Nome Da Variável = salario.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.


if (salario == 280):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    reajuste = (salario * 20) / 100
        # Nome Da Variável = reajuste.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario * 20 / (Dividido Por: ) -> 100

    total = salario + reajuste
        # Nome Da Variável = total.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario + (Valor Da Variável: ) -> reajuste

    print ("=" * 60)

    print ("- O Salario Do Funcionario ({}) Éra De: R${} ".format(nome, salario))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O percentual de aumento aplicado foi de 20%")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("-" * 60)

    print ("- O reajuste do funcionario ({}), será de: R${} ".format(nome, reajuste))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O novo salario de ({}) será de: R${} ".format(nome, total))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("=" * 60)

elif (salario >= 281) or (salario <= 700):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    reajuste = (salario * 15) / 100
        # Nome Da Variável = reajuste.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario * 15 / (Dividido Por: ) -> 100

    total = salario + reajuste
        # Nome Da Variável = total.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario + (Valor Da Variável: ) -> reajuste

    print ("=" * 60)

    print ("- O Salario Do Funcionario ({}) Éra De: R${} ".format(nome, salario))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O percentual de aumento aplicado foi de 15%")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("-" * 60)

    print ("- O reajuste do funcionario ({}), será de: R${} ".format(nome, reajuste))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O novo salario de ({}) será de: R${} ".format(nome, total))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("=" * 60)

elif (salario >= 701) or (salario <= 1500):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    reajuste = (salario * 10) /  100
        # Nome Da Variável = reajuste.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario * 10 / (Dividido Por: ) -> 100

    total = salario + reajuste
        # Nome Da Variável = total.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario + (Valor Da Variável: ) -> reajuste

    print ("=" * 60)

    print ("- O Salario Do Funcionario ({}) Éra De: R${} ".format(nome, salario))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O percentual de aumento aplicado foi de 10%")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("-" * 60)

    print ("- O reajuste do funcionario ({}) será de: R${} ".format(nome, reajuste))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O novo salario de ({}) será de: R${} ".format(nome, total))
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("=" * 60)

elif (salario > 1501):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    reajuste = (salario * 5) / 100
        # Nome Da Variável = reajuste.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario * 5 / (Dividido Por: ) -> 100

    total = salario + reajuste
        # Nome Da Variável = total.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> salario + (Valor Da Variável: ) -> reajuste

    print ("=" * 60)

    print ("- O Salario Do Funcionario ({}) Éra De: R${} ".format(nome, salario))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O percentual de aumento aplicado foi de 5%")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("-" * 60)

    print ("- O reajuste do funcinario ({}) será de: R${} ".format(nome, reajuste))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("-" * 60)

    print ("- O novo salario de ({}) será de: R${} ".format(nome, total))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("=" * 60)

print ("*** Reajuste Concluido Com Sucesso!!! ***")

print ("=" * 60)

