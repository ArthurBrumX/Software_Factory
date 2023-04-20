# 11 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE A MÉDIA DOS NÚMEROS.

def media(lista):
  
  soma = 0

  for num in lista:

    soma += num

  return print(soma/len(lista))

media([10,10,52,1,15])