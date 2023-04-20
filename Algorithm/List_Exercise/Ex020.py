# 20 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este é ou não bissexto.

print ("=" * 60)

print ("*** Ano Bissexto! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)


ano = int(input("* Digite um ano para verificar Se é bissexto: "))
    # Nome Da Variável = ano.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

ano_bi = ano % 4
    # Nome Da Variável = ano_bi.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> ano % (Resto Da Divisão por: ) -> 4

if (ano_bi == 0):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print (" ")

    print("- O Ano Digitado é Bissexto!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

else:
    # Else = Senão
        # Se Nehuma Das Condição for Atendida, Execute o Codigo Abaixo.

    print (" ")

    print("- O Ano Digitado Não é Bissexto!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)

















