# 7 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE UMA LISTA COM APENAS OS NÚMEROS ÍMPARES.

def lista_impares(lista):
  
  impares = []

  for num in lista:
    if  num % 2 != 0:
      
      impares.append(num)

  return print(impares)

lista_impares ([2,3,5,7])