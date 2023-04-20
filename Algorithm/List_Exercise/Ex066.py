# 66 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma 
# taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou 
# iguale a população do país B, mantidas as taxas de crescimento.

print ("=" * 60)

print ("*** Taxa Anual De Crescimento! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

contador = 0
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

anos = 0 
    # Nome Da Variável = anos.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

pais_a = 80000
    # Nome Da Variável = pais_a.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

pais_b = 200000
    # Nome Da Variável = pais_b.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

crescimento_a = pais_a * 3 /100
    # Nome Da Variável = crescimento_a.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> pais_a * 3 / 100

crescimento_b = pais_b * 1.5 / 100
    # Nome Da Variável = crescimento_b.
    # Função = Calculo Com Variáveis
    # Calculo: (Valor da Variável: ) -> pais_b * 1.5 / 100

taxa_anual_p_a = crescimento_a
    # Nome Da Variável = taxa_anual_p_a.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

taxa_anual_p_b = crescimento_b
    # Nome Da Variável = taxa_anual_p_b.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (pais_b > pais_a):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    contador = contador + 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    anos = anos + 1
        # Nome Da Variável = crescimento_a.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> anos + 1

    pais_a = pais_a + crescimento_a + taxa_anual_p_a
        # Nome Da Variável = pais_a.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> pais_a + (Valor da Variável: ) -> crescimento_a + (Valor da Variável: ) -> taxa_anual_p_a

    print ("- No {}° ano seram {} habitantes!!".format(contador, pais_a))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- Seram precisos {} anos para se igualar ao pais B!! ".format(anos))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)


