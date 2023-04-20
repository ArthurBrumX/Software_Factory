# 3 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE O MAIOR NÚMERO DA LISTA.



def maior_numero(numero):
    
    maior = numero[0]

    for num in numero:
        if num > maior:
            maior = num 

    return print("O maior Numero é: ",maior)


maior_numero([3,5,1,2,4])