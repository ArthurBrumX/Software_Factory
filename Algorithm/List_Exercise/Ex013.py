# 13 - Faça um algoritmo que leia o número digitado e verifique se é par ou ímpar.


print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
print ("*** Par Ou Impar! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Descubra Se O Número é Par Ou Impar! *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

numero = float(input("Digite Um Número: "))
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

resultado = numero % 2
    # Nome Da Variável = resultado.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> Numero % (Resto da divisao Por: ) -> 2

if (resultado == 0):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("*** Usuário, o Número {} É Um número Par!! ***".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

elif (resultado == 1):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo. 

    print ("-" * 60)

    print ("*** Usuário, o Número {} É Um número Impar!! ***".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

print ("=" * 60)
