# 21 - Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, 
# calcule e mostre o valor da comissão e o salário final do funcionário.

print ("=" * 60)

print ("*** lets-go Restaurante ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Reajuste Salarial *")
    # Apresentação Ao Usuário.

print ("¨" * 60)


funcionario = (input("* Digite o Nome Do Funcionario: "))
    # Nome Da Variável = funcionario.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

salario = float(input("* Digite o Salário De {}: ".format(funcionario)))
    # Nome Da Variável = salario.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

vendas = float(input("* Digite qual o valor da Venda mensal de {}: ".format(funcionario)))
    # Nome Da Variável = vendas.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

comissao = (vendas * 4) / 100
    # Nome Da Variável = comissao.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> vendas * 4  (Dividido por: ) -> 100

sal_liquido = salario + comissao
    # Nome Da Variável = salario_liquido.
        # Função = Calculo Com Variáveis.
            # Calculo: (Valor da Variável: ) -> salario + (Valor da Variável: ) -> comissao

print ("=" * 40 )

print ("- O Salário Mensal De {} Será De: R${}".format(funcionario, sal_liquido))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 40 )



