# 84 - Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.

print ("=" * 60)

print ("*** Verificador De Números ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

numeros = [5,8,3,2,8,9,1,4,6,0]
    # Vetor
        # Comando para armazenar informacoes como uma lista

valor = int(input("* Digite um numero: "))
    # Nome Da Variável = valor.
    # Tipo Da Variável = Int (Inteiro).
    # Função = Entrada De Dados

print ("=" * 60)

if (numeros.count(valor) >= 1):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print("- O Número {} Está Dentro Da Lista!".format(valor))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

    print ("=" * 60)

elif (numeros.count(valor) < 1):
    # Elif = SeNão se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("* O Número {} Não Está Na Lista!".format(valor))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

    print ("=" * 60)
