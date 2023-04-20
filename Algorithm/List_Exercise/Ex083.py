# 83 - Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. 
# Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.

print ("=" * 60)

print ("*** Somando Números ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

numeros = []
    #Vetor
        # Comando para armazenar informacoes como uma lista
contador = 1
    # Nome Da Variável = contador.
    # Tipo Da Variavel = Int (Inteiro).
    # Função = Atribuição De Valor.

print ("Digite 5 Numeros!!")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

while (contador < 6):

    entrada = float(input("* Digite  o {}° Número: ".format(contador)))
        # Nome Da Variável = entrada.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    contador += 1
        # Nome Da Variável = contador.
        # Função = Calculo Com Variáveis
        # Calculo: (Valor da Variável: ) -> contador + 1

    numeros.append(entrada)
        # Append = Acrecentar

soma = sum(numeros)
    # sum = soma de todos os elementos da lista.

print ("=" * 60)

print ("- Os Numeros Digitados São: ")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

for n in (numeros):

    print ("- {}".format(n))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("- A soma Dos Números Digitados é: {}".format(soma))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)
