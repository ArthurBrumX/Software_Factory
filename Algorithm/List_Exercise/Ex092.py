# 92 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.As perguntas são:
# • "Telefonou para a vítima?"
# • "Esteve no local do crime?"
# • "Mora perto da vítima?"
# • "Devia para a vítima?"
# • "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 
# questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print ("=" * 60)

print ("*** Investigação Criminal ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

sim = 0
    # Nome Da Variável = sim.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

print ("=" * 60)

perguntas = ['Telefonou para a vitima? [s/n]: ',
             'Esteve no local do crime? [s/n]: ',
             'Mora perto da vitima? [s/n]: ',
             'Devia para a vitima? [s/n]: ',
             'Já trabalhou com a vítima? [s/n]: ']
                # Lista Para armazenar Valores
            
print ("=" * 60)

for i in range(len(perguntas)):
    # For = Para

    resposta = input(perguntas[i])
        # Nome Da Variável = resposta.
        # Tipo Da Variavel = str (String).
        # Função = Entrada De Dados.

    if (resposta == 's'):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        sim += 1
            # Nome Da Variável = sim.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> sim + 1

print ("=" * 60)

if (sim == 2):
    # If = Se
          # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print('\nVocê é Suspeito!')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (sim > 2 and sim <= 4):
    # Elif = Senao
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print('\nVocê é Cumplice!')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif sim == 5:
    # Elif = Senao
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print('\nVocê é o Assassino!')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

else:
    # Else = SeNão
          # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print('\nVocê é Inocente!')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)

