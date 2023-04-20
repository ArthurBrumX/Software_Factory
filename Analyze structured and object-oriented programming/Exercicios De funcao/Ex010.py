# 10 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE O SEGUNDO MENOR NÚMERO DA LISTA.

def segundo_menor(lista):
  
  menor = lista[0]

  for num in lista:

    if num != menor:
      
      if menor == min(lista):

        menor = num

      elif num < menor:

        menor = num
        
  return menor

segundo_menor([2,5,2,3,9,7,2])