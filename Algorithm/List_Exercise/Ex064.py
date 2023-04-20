# 64 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:

# • Código da cidade;
# • Número de veículos de passeio (em 1999);
# • Número de acidentes de trânsito com vítimas (em 1999).

# Deseja-se saber:

# • Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# • Qual a média de veículos nas cinco cidades juntas;
# • Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

print ("=" * 60)

print ("*** Estatísticas De Acidentes ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

codigo_Cidade = int(input("Digite o código da cidade: "))
    # Nome Da Variável = codigo_Cidade.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

quant_Veiculos = int(input("Digite o número de veículos na cidade: "))
    # Nome Da Variável = quant_Veiculos.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.

quant_Acidentes = int(input("Digite o número de acidentes com vitimas da cidade: "))
    # Nome Da Variável = quant_Acidente.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados.


print ("=" * 60)

indice_Acidente = float(quant_Acidentes) / quant_Veiculos
    # Nome Da Variável = indice_Acidente.
    # Função = Calculo Com Variáveis
     # Calculo: (Valor da Variável: ) -> quant_Acidentes (convertido Para o Tipo Real) / (Valor da Variável: ) -> quant_Veiculos

maior_Indice = indice_Acidente
    # Nome Da Variável = maior_Indice.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

maior_Indice_Codigo = codigo_Cidade
    # Nome Da Variável = maior_Indice_Codigo.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

menor_Indice = indice_Acidente
    # Nome Da Variável = menor_Indice.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

menor_Indice_Codigo = codigo_Cidade
    # Nome Da Variável = menor_Indice_Codigo.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

soma = quant_Veiculos
    # Nome Da Variável = soma.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

soma_Veiculos_2000 = 0
    # Nome Da Variável = soma_Veiculos_2000.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

divisor_Media_2000 = 1
    # Nome Da Variável = divisor_Media_2000.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

if (quant_Veiculos < 2000):
	# If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 
	
	soma_Veiculos_2000 = soma_Veiculos_2000 + quant_Acidentes
        # Nome Da Variável = soma_Veiculos_2000.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> soma_Veiculos_2000 + (Valor da Variável: ) -> quant_Acidentes

	divisor_Media_2000 = divisor_Media_2000 + 1
        # Nome Da Variável = divisor_Media_2000.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> divisor_Media_2000 + 1

a = 1
    # Nome Da Variável = a.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

while (a < 5):
	# While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.
	
	codigo_Cidade = int(input("Digite o código da cidade: "))
        # Nome Da Variável = codigo_Cidade.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

	quant_Veiculos = int(input("Digite o número de veículos na cidade: "))
        # Nome Da Variável = quant_Veiculos.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.

	quant_Acidentes = int(input("Digite o número de acidentes com vítimas da cidade: "))
        # Nome Da Variável = quant_Acidentes.
        # Tipo Da Variável = Int (Inteiro).
        # Função = Entrada De Dados.
	
	print ("=" * 60)

	indice_Acidente = float(quant_Acidentes) / quant_Veiculos
        # Nome Da Variável = indice_Acidente.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> quant_Acidentes (convertido Para o Tipo Real) / (Valor da Variável: ) -> quant_Veiculos
	
	soma = soma + quant_Veiculos
        # Nome Da Variável = soma.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> soma + (Valor da Variável: ) -> quant_Veiculos

	if (indice_Acidente > maior_Indice):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 
		
		maior_Indice = indice_Acidente
            # Nome Da Variável = maior_Indice.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

		maior_Indice_Codigo = codigo_Cidade
            # Nome Da Variável = maior_Indice_Codigo.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

	if (indice_Acidente < menor_Indice):
		# If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 
		
		menor_Indice = indice_Acidente
            # Nome Da Variável = menor_Indice.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

		menor_Indice_Codigo = codigo_Cidade
            # Nome Da Variável = menor_Indice_Codigo.
            # Tipo Da Variavel = Int (Inteiro).
            # Função = Atribuição De Valor.

	if (quant_Veiculos < 2000):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 
		
		soma_Veiculos_2000 = soma_Veiculos_2000 + quant_Acidentes
            # Nome Da Variável = soma_Veiculos_2000.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> soma_Veiculos_2000 + (Valor da Variável: ) -> quant_Acidentes

		divisor_Media2000 = divisor_Media_2000 + 1
            # Nome Da Variável = sdivisor_Media2000.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> divisor_Media_2000 + 1

	a = a + 1
        # Nome Da Variável = a.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> a + 1
	
print ("=" * 60)

print ("- Menor índice: %.2f" % (menor_Indice))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # %.2f = Vai Alocar Uma Variavel 
        # Sendo Que Mostra-rá apenas 2 unidades apos o ponto.
        # Ex: 0.00
      
print ("Código da cidade: %d" % (menor_Indice_Codigo)) 
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # %.2f = Vai Alocar Uma Variavel 
    # O %d é um placeholder (marcador de posição). 
        # Ele é usado para reservar valores (números) em um vetor.

print ("- Maior índice: %.2f" %(maior_Indice))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # %.2f = Vai Alocar Uma Variavel 
        # Sendo Que Mostra-rá apenas 2 unidades apos o ponto.
        # Ex: 0.00
       
print ("Código da cidade: %d" % (maior_Indice_Codigo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # %.2f = Vai Alocar Uma Variavel 
    # O %d é um placeholder (marcador de posição). 
        # Ele é usado para reservar valores (números) em um vetor.

print ("- Média de veículos nas %d cidades = %d veículos" % (a,(float(soma)/a)))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # %.2f = Vai Alocar Uma Variavel 
    # O %d é um placeholder (marcador de posição). 
        # Ele é usado para reservar valores (números) em um vetor.

print ("- Média de acidentes em cidades com menos de 2000 veículos: %.1f" % (float(soma_Veiculos_2000) / divisor_Media_2000))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # %.2f = Vai Alocar Uma Variavel 
        # Sendo Que Mostra-rá apenas 1 unidades apos o ponto.
        # Ex: 0.0

print ("=" * 60)
