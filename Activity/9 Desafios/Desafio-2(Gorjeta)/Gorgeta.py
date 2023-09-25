# 2- Menu com opções de um cardápio de restaurante para uma pessoa (Coloque no 
# mínimo 5 opções. Ex: Bife acebolado R$15,00; Lasanha R$25,00). A pessoa vai 
# escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a 
# seguinte pergunta ao usuário, “Aceita pagar a gorjeta do garçom 10% sobre o valor 
# do prato”. Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso 
# contrário, mostrar o valor final (somente o valor do prato).

print(50*"=")
print ("Restaurante Hunter")
print(50*"=")
print("1 - Bife Acebolado.......................R$15\n"
      "2 - Lasanha..............................R$25\n"
      "3 - Macarronada..........................R$10\n"
      "4 - Isca De Frango.......................R$17\n"
      "5 - Bife a Role..........................R$20\n")
print(50*"=")

pedido = int(input("Digite o Numero Do Seu Pedido: "))

print(50*"=")

if(pedido == 1):
    valor_conta = 15
elif(pedido == 2):
    valor_conta = 25
elif(pedido == 3):
    valor_conta = 10
elif(pedido == 4):
    valor_conta = 17
elif(pedido == 5):
    valor_conta = 20

pergunta = input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato [S/N]: ")

print(50*"=")

if (pergunta == "S") or (pergunta == "sim"):
    gorjeta = valor_conta * 10 / 100
    totalValorConta = gorjeta + valor_conta
    print(f"O total da conta deu: R${totalValorConta}")

elif(pergunta == "N") or (pergunta == "não"):
    totalValorConta = valor_conta
    print(f"O total da conta deu: R${totalValorConta}")

print(50*"=")









