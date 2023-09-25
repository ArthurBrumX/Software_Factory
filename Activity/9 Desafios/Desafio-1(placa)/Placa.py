# 1- O usuário deverá escolher uma opção de acordo com o último número da placa 
# do carro e mostre uma mensagem dizendo em que dia da semana não poderá circular.

# 1- 2 “Não Circular 2ª Feira”
# 3 - 4 “Não Circular 3ª Feira”
# 5 - 6 “Não Circular 4ª Feira”
# 7- 8 “Não Circular 5ª Feira”
# 9 - 0 “Não Circular 6ª Feira”


finalPlaca = int(input("Digite qual o ultimo numero da placa do seu veiculo: "))

if (finalPlaca == 1) or (finalPlaca == 2):
    print("Não Circular 2º feira!")

elif(finalPlaca == 3) or (finalPlaca == 4):
    print("Não circular 3º feira!")

elif(finalPlaca == 5) or (finalPlaca == 6):
    print("Não circular 4º feira!")

elif(finalPlaca == 7) or (finalPlaca == 8):
    print("Não circular 5º feira!")

elif(finalPlaca == 9) or (finalPlaca == 0):
    print("Não circular 6º feira!")