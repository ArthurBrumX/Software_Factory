# 86 - Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o salário da 
# pessoa, o algoritmo deverá escrever “Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado". Independente de conceder ou não o financiamento, 
# o algoritmo escreverádepois a frase "Obrigado porConsultar"

print ("=" * 60)

print ("*** Financiamento!***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

salario = float(input("* Digite Seu Salário: "))
    # Nome Da Variável = salario.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados

financiamento = float(input("* Digite o valor Do Financiamento: "))
    # Nome Da Variável = Financiamento.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados

print ("=" * 60)

teste_financiamento = 5 * salario 
    # Nome Da Variável = teste_financiamento.
    # Função = Calculo Com Variáveis
    # Calculo: 5 * (Valor da Variável: ) -> salario 

if (financiamento <= teste_financiamento):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print("- Financiamento Concedido!!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("- Obrigado por Consulta")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)

else:
    # else = SeNão
        # Se Nenhuma Condição for Atendida, Execute o Codigo Abaixo.

    print ("- Financiamento Negado!!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("- Obrigado por Consulta")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print ("=" * 60)