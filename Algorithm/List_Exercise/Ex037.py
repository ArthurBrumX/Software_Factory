# 37 - A padaria Super Pão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pãozinho custa R$ 1,00 e a broa custa R$ 3,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar 
# numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades 
# de pães e de broas, e depois calcular os dados solicitados.

print ("=" * 60)

print ("*** Padaria Super Pão ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo!! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

paozinho = 1
    # Nome Da Variável = paozinho.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

broa = 3.50
    # Nome Da Variável = Broa.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

venda_1 = float(input("* Qual a Quantidade de Pães vendidos No Dia: R$ "))
    # Nome Da Variável = venda_1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

venda_2 = float(input("* Qual a Quantidade de Broas vendidos No Dia: R$ "))
    # Nome Da Variável = venda_2.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

total_venda = venda_1 + venda_2
    # Nome Da Variável = total_venda.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> venda_1 + (Valor da Variável: ) -> venda_2

poupanca = total_venda * 10 / 100
    # Nome Da Variável = poupanca.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> total_venda * 10 / 100
    
print ("=" * 60)

print ("- O total da venda do dia é: R${}".format(total_venda))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("- O 10% que será guardado na poupança será de: R${}".format(poupanca))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)