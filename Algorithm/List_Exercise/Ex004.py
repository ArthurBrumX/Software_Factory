# 4 - Faça um algoritmo que leia o nome, a placa do carro, o modelo do carro e a cor do carro. Posteriormente imprima o resultado de cada variável linha abaixo de linha.

print ("=" * 60)

print ("*** Sitema De Fiscalização ***")
print ("* Preencha os Dados Do Seu Veiculo! *")
    # Apresentação Ao Usuário.

print ("=" * 60)

nome_usuario = input("-Qual Nome Completo Do Proprietário: ")
    # Nome Da Variável = nome_usuario.
    # Tipo Da Variave = Str (String).
    # Função = Entrada De Dados.

placa = (input("-Qual a Placa Do Veiculo: "))
    # Nome Da Variável = placa.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

modelo_veiculo = input("-Qual a Marca/Modelo Do Veiculo: ")
    # Nome Da Variável = modelo_veiculo.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

cor = input("-Qual a Cor Do Veículo: ")
    # Nome Da Variável = cor.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("* Nome Completo: {}".format(nome_usuario))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)


print ("* Placa Do Veiculo: ({})".format(placa))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)


print ("* Marca/Modelo Do veiculo: ({})".format(modelo_veiculo))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)


print ("* Cor Do Veiculo: {}".format(cor))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
        # Ex: .format(Nome_da_Variável)

print ("-" * 60)

print ("*** Fiscalização Concluida Com Sucesso! ***")
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.


print ("=" * 60)

