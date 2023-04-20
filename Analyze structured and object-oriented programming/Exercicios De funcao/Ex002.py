# 2 - CRIE UMA FUNÇÃO QUE RETORNE O MAIOR VALOR ENTRE DOIS NÚMEROS.

def resultado():
    numero_1 = float(input("Digite um numero: "))
    numero_2 = float(input("Digite Outro NUmero: "))

    if (numero_1 > numero_2):
        print ("O Maior Numero é: ",numero_1)

    elif (numero_2 > numero_1):
        print ("O Maior Numero é: ",numero_2)

resultado()


