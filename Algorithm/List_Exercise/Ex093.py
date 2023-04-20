# 93 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as 
# temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

print ("=" * 60)

print ("*** Temperatura Media Dos Meses!!! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

temperatura_do_mes = []
    # Lista = Armazna Dados Dentro

meses_do_ano = ['Janeiro', 'Fevereiro', 'Março','Abril',
                'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                'Outubro', 'Novembro', 'Dezembro']
                # Lista = Armazna Dados Dentro

for i in range(12):
    # For = Para

    print(f'\nMês de: {meses_do_ano[i]}')
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
    
    print ("=" * 60)
    
    media = temperatura_do_mes.append(float(input('Digite a temperatura média em °C: ')))
        # Nome Da Variável = media.
        # Tipo Da Variavel = Float (Real).
        # Função = Entrada De Dados.

media_anual = sum(temperatura_do_mes) / 12
    # Nome Da Variável = media_anual.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> temperatura_do_mes + 12

print("=" * 60)

print("Média Anual de Temperatura: {}°C".format(media_anual))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print("=" * 60)

for i in range(12):
    # For = Para

    if (temperatura_do_mes[i] > media_anual):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("=" * 60)

        print("Temperatura a cima da média no mês: {} com Temperatura de: {}".format(meses_do_ano, temperatura_do_mes))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

print ("=" * 60)



