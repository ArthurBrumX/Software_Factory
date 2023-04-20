# 59 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

print ("=" * 60)

print ("*** Intervalo Entre Números ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

numero_1 = int(input("* Digite um numero: "))
    # Nome Da Variável = numero_1.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

numero_2 = int(input("* Digite outro numero: "))
    # Nome Da Variável = numero_2.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

while (numero_2 < numero_1):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.
	
	numero_1 = int(input("* Digite um numero: "))
        # Nome Da Variável = numero_1.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.
	
	numero_2 = int(input("* Digite outro numero: "))
        # Nome Da Variável = numero_2.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.
	
else:
	# else = seNão
        # Se Nenhuma Condição for Atendida, Execute o Codigo Abaixo.
	
	for valor in range(numero_1,numero_2 , 1):
		
		print(valor)
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

print ("=" * 60)

