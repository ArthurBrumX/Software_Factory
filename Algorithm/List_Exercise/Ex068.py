# 68 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

print ("=" * 60)

print ("*** Contagem!! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

print ("- De 1 a 20, Um Abaixo Do Outro!! \n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

for n in range (1, 21):
    # For = Durante
        # A Varável (n) Vai de (1 Até 20)

    print (n)
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)

print ("- De 1 a 20, Um Ao Lado Do Outro!! \n")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.

print (' '.join(str(n) for n in range (1,21)))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    #.join = vai iterar sobre os elementos criando uma string única, e o print vai imprimir essa string.
    # ou
        # print (n, ' ', end = ' ')

print ("=" * 60)









