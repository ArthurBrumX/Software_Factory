# 90 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas 
# vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

# • $200 - $299
# • $300 - $399
# • $400 - $499
# • $500 - $599
# • $600 - $699
# • $700 - $799
# • $800 - $899
# • $900 - $999
# • $1000 em diante

# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

print ("=" * 60)

print ("*** Casa Das Cores!! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

salarios = [[200,299],[300,399],[400,499],[500,599],[600,699], [700,799],[800,899],[900,999]]
    # Vetor
        # Comando para armazenar informacoes como uma lista

quantidade = [0,0,0,0,0,0,0,0,0]
    # Vetor
        # Comando para armazenar informacoes como uma lista

salarios = []
    # Vetor
        # Comando para armazenar informacoes como uma lista

venda_mensal = True
    # Nome Da Variável = contador_1.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (venda_mensal != 0):
    # While = Enquanto

    venda_mensal = float(input("Digite a valor das vendas: $ "))
        # Nome Da Variável = venda_mensal.
        # Tipo Da Variavel = float (real).
        # Função = Entrada De Dados.

    if (venda_mensal == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        break
            # Break = Quebre o codigo.

    else:
        # Else = SeNão
            # Se Nenhuma Condição for Atendida, Execute o Codigo Abaixo.

        salario = (venda_mensal * 0.09) + 200
            # Nome Da Variável = salario.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> dvenda_mensal * 0.09 + 200

        print(f'R$ {salario:.2f}')
<<<<<<< HEAD
        if salario < 1000:
            
            for i in range(len(faixas_salarios)):

                if salario >= faixas_salarios[i][0] and salario < faixas_salarios[i][1]:

                    quantidades[i] += 1

=======
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

        if (salario < 1000):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            for i in range(len(salarios)):
                # For = Para

                if (salario >= salarios[i][0] and salario < salarios[i][1]):
                    # If = Se
                    # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

                    quantidade[i] += 1
>>>>>>> 85aad7b3c9678b7357b50317498a6df4c8acda15
        else:
            # Else = SeNão
            # Se Nenhuma Condição for Atendida, Execute o Codigo Abaixo.

            quantidade[8] += 1

print("=" * 60)

for i in range(len(salarios)):
    # For = Para

    print("Faixas de Salários:")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    print(f"Entre $ {salarios[i][0]:.2f} e R$ {salarios[i][1]:.2f}: {quantidade[i]}")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print(f'Salarios maiores que $1000: {quantidade[8]}')
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)
