# 25 - Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por R$10,00, R$12,00 e R$15,00. Faça um algoritmo em que o 
# usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, o algoritmo informe qual o valor total da compra.

print ("=" * 60)

print ("*** Enilda Estilos! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Não Perca Nossas Promoções De Camisas! *")
print ("* Qualquer Camisa Masculina Ou Feminina Por: ")
    # Apresentação Ao Usuário.

print ("=" * 60)

print ("* Pequena: R$ 10,00! *")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("* Média: R$ 12,00! *")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("* Grande: R$ 15,00! *")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)


c_pequenas = float(input("* Quantas camisas pequenas vai querer: "))
    # Nome Da Variável = c_pequenas.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

c_medias = float(input("* Quantas camisas medias vai querer: "))
    # Nome Da Variável = c_medias.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

c_grandes = float(input("* Quantas camisas Grandes vai querer: "))
    # Nome Da Variável = c_grandes.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.


print ("=" * 60)

p = 10
    # Nome Da Variável = p.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

m = 12
    # Nome Da Variável = m.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

g = 15
    # Nome Da Variável = g.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

total_p = c_pequenas * p
    # Nome Da Variável = total_p.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> c_pequenas * (Valor Da Variável: ) -> p

total_m = c_medias * m
    # Nome Da Variável = total_m.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> c_medias * (Valor Da Variável: ) -> m

total_g = c_grandes * g
    # Nome Da Variável = total_g.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> c_grandes * (Valor Da Variável: ) -> g

total_compra = total_p + total_m + total_g
    # Nome Da Variável = total_compra.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> total_p + (Valor Da Variável: ) -> total_m + (Valor Da Variável: ) -> total_g

print ("- A Sua Compra Foi No Total De R${} Reais!!".format(total_compra))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("**** Compra Realizada Com Sucesso!! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("*** Volte Sempre!!! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)