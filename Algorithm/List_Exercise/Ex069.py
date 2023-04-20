# 69 - Faça um programaque leia 5 números e informe a soma e a média dos números.

print ("=" * 60)

print ("*** Média!!! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

numero = 0
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

soma = 0
    # Nome Da Variável = soma.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (numero < 5):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    n1 = float(input("* Digite Um numero: "))
        # Nome Da Variável = senha.
        # Tipo Da Variável = float (Real).
        # Função = Entrada De Dados.

    print ("=" * 60)

    soma = soma + n1
        # Nome Da Variável = soma.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> soma + (Valor da Variável: ) -> n1

    numero = numero + 1
        # Nome Da Variável = numero.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> numero + 1

media = soma / 5
    # Nome Da Variável = media.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> soma / 5 

print ("- A Média De {} é Igual : {}".format(n1, media))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)











