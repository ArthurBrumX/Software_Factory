# 6 - CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE STRING COMO PARÂMETRO E RETORNA A STRING MAIS LONGA

def string_longa(lista):
  
  mais_longa = lista[0]

  for i in lista:

    if len(i) > len(mais_longa):
      
      mais_longa = i
      
  return mais_longa 

string_longa(['ana', 'joana'])