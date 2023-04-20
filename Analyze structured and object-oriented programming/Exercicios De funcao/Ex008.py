# 8 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS COMO PARÂMETRO E RETORNE O NÚMERO DE OCORRÊNCIA DE UM DETERMINADO NÚMERO DA LISTA.

def qtd_ocorrencia(lista, num):
  
  contador = 0

  for n in lista:

    if n == num:
      
      contador += 1
      
  return contador

qtd_ocorrencia([2,5,6,7,2,7,2,7],7)