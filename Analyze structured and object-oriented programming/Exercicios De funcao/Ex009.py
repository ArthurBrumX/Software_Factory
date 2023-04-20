# 9 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE UMA LISTA COM APENAS NÚMEROS MENORES QUE 10.


def numeros(lista):

    menor = []

    for num in lista:

        if num < 10:

            menor.append(num)

    return print(menor)
    
numeros ([21,20,4,6,10,3,9,0])



