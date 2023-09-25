# 3 - O programa de fidelidade de uma determinada livraria premia seus clientes de 
# acordo com o número de livros comprados a cada semestre. Os pontos são atribuídos 
# da seguinte forma:

# •Se um cliente comprar 0 livros, ele ganhará 0 pontos.
# •Se um cliente comprar 1 livro, ele ganhará 5 pontos.
# •Se um cliente comprar 2 livros, ele ganhará 15 pontos.
# •Se um cliente comprar 3 livros, ele ganhará 30 pontos.
# •Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
# Lista de brindes: 

# De 20 à 30 pontos o cliente poderá escolher entre: Uma Ecoa OU Caneta 
# personalizada De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor 
# máximo de R$30,00) OU Luminária de cabeceira. Acima de 65 o cliente poderá 
# escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank.

# Obs: Os pontos são acumulativos, e contado a cada compra realizada pelo cliente. 
# Ex: Se o cliente na semana 1 comprar 2 livros de uma única vez ele receberá 15 
# pontos, se na semana 2 ele comprar 1 único livro receberá 5 pontos totalizando 20 
# pontos em duas semamas. Crie um programa que leia o número de livros comprado 
# por um usuário e exiba o número de pontos correspondentes e qual brinde ele poderá 
# escolher.

comprar = input("Deseja Comprar: ")
pontos = 0
quantCompras = 0

while comprar == "sim":

    quantLivros = int(input("Quantos livros Vai Comprar dessa vez: "))

    if quantLivros == 0:
        print ("Voçê Comprou 0 Livros e Guanhou 0 Pontos!")
        pontos += 0

    elif quantLivros == 1:
        print("Voçê Comprou 1 Livros e Guanhou 5 pontos!")
        pontos += 5
        quantCompras += 1

    elif quantLivros == 2:
        print("Voçê Comprou 2 Livos e Guanhou 15 Pontos!")
        pontos += 15
        quantCompras += 1

    elif quantLivros == 3:
        print("Voçê Comprou 3 Livros e Guanhou 30 Pontos!")
        pontos += 30
        quantCompras += 1

    elif quantLivros >= 4:
        print (f"Voçê Comprou {quantLivros} Livros e Guanhou 60 Pontos!")
        pontos += 60
        quantCompras += 1

    comprar_1 = input("Deseja Comprar Novamente: ")

    if comprar_1 == "nao":
        break

print(f"Voçê Fez o total de {quantCompras} Compras Efetuadas!")
print(f"Voçê Tem o Total De {pontos} Pontos Acumulados!")

if pontos == 0:
    print("Lamento Mas voçê Não Tem Pontos Suficiente Para Escolher Um Premio!")
elif pontos >= 20 or pontos <= 34:
    print("poderá escolher entre: Uma Ecoa OU Caneta personalizada")
elif pontos >= 35 or pontos <=64:
    print("poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.")
elif pontos >= 65:
    print("poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank.")

escolha = input("Qual Premio Vai escolher: ")

print(f"Parabens Voce Escolheu um {escolha}!")
