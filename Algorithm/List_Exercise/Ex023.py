# 23 - A granja TecFrango possui um controle automatizado de cada frango da sua produção. No pé direito do frango há um anel com um chip de identificação, no pé 
# esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa R$ 4,00 e o anel de alimento custa R$ 3,50, faça um algoritmo 
# para calcular o gasto total da granja (com base na quantidade de frangos digitada pelo usuário) para marcar todos os seus frangos.

print ("=" * 60)

print ("*** Granja TecFrango ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("*  Controle Automatizado *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

n_galinhas = int(input("Digite o Número De Galinhas Presentes No Galinheiro: "))
    # Nome Da Variável = n_galinhas.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

p_direito = 4.00
    # Nome Da Variável = p_direito.
    # Função = Atribuição De Dados.
        # p_direito = 4.00

p_esquerdo = 2 * 3.50
    # Nome Da Variável = p_esquerdo.
    # Função = Atribuição De Dados.
        # p_direito = 2 * 3.50


galinha = p_direito + p_esquerdo
    # Nome Da Variável = galinha.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> p_direito + (Valor da Variável: ) -> p_esquerdo

total = n_galinhas * galinha
    # Nome Da Variável = total.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> n_galinhas * (Valor da Variável: ) -> galinha

print ("=" * 60)

print ("O Total Gasto No Galinheiro Será De: R$ {}!!".format(total))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)
