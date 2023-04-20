# 7 - Faça um algoritmo que calcule a área de um triângulo. Posteriormente imprima o resultado.

print ("=" * 60)

print ("*** Calculo De Triângulo ***")
print ("*** Bem-vindo Usuário! ***")
    # Boas-Vindas Ao Usuário!

print("=" * 60)

print ("* Vamos Calcular a Área De Um Retângulo! *")
    # Função = Saida De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)

base = float(input("* Digite a Base do Triângulo: "))
    # Nome Da Variável = base.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

altura = float(input("* Digite a Altura Do Triângulo: "))
    # Nome Da Variável = altura.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

area = (base * altura) / 2
    # Nome Da Variável = area.
        # Função = Calculo Com Variáveis.
            # Calculo: (Valor da Variável: ) -> base * (Valor Da Variável: ) -> altura / 2.

print ("-A Área do Triangulo é: {}".format(area))
    # Função = Saida De Dados.
    # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}
        # Ex: .format(Nome_da_Variável).

print("=" * 60)

print ("*** Fim Do Calculo! ***")
    # Função = Saida De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)