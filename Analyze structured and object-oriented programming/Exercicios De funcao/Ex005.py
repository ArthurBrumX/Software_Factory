# 5 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE PALVRAS COMO PARÂMETRO E RETORNE UMA LISTA COM PALAVRAS QUE COMEÇAM COM A LETRA "A".

def lista_de_palavra (palavras):

    lista = []

    for num in palavras:
        
        if num [0] == "a" or num [0] == "A":
            lista.append(num)
    print (lista)

lista_de_palavra(["ana", "pedro", "Antonio", "marcos", "Rafaela", "Angelo", "Arthur"])

