# 4 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE UMA LISTA COM APENAS NÚMEROS PARES.

def lista_pares(lista):
  
  pares = []

  for num in lista:
    if  num % 2 == 0:
      
      pares.append(num)

  return print(pares)

lista_pares ([8,6,2,20])