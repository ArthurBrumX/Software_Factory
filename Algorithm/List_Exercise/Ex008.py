# 8 - Faça um algoritmo que calcule o custo estimado de uma viagem de carro. Posteriormente imprima o resultado.

print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
print ("* Vamos Calcular o Custo de Uma viagem de carro!* ")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

local = input("* Qual Será o Destino Da Viagem: ")
    # Nome Da Variável = local.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

gasolina = input("* Qual é o Tipo De Gasolina Usado: ")
    # Nome Da Variável = gasolina.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

if (gasolina == "Aditvada") or (gasolina == "adtivada"):
    # Estrutura De Repetição.
        # Só Será Exibida Caso Atenda a Um Evento.

    litro = float(input("* Quantos kilometros Seu Veiculo Faz Com 1 Litro De Gasolina: "))
        # Nome Da Variável = litro.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    distancia = float(input("* Qual a Distancia Em kilomentros Até o Destino: "))
        # Nome Da Variável = distancia.
        # Tipo Da Variável = Float(Real).
        # Função = Entrada De Dados.

    gasolina_aditvada = 6.73
        # Atribuindo um Valor a Uma Variavel.

    destino = litro * distancia
        # Nome Da Variável = destino.
        # Função = Calculo De Variáveis.
        # (Valor Da Variável) -> litro * (Valor Da Variável) -> distancia.

    valor = destino * gasolina_aditvada
        # Nome Da Variável = valor.
        # Função = Calculo De Variáveis.
        # (Valor Da Variável) -> destino * (Valor Da Variável) -> gasolina_aditvada.

    print ("=" * 60)

    print ("-Se não Houver Nenhum Imprevisto O Valor até {} é de R${}".format(local, valor))
        # Função = Entrada De Dados.
        # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (gasolina == "Comum") or (gasolina == "comum"):
    # Estrutura De Repetição.
        # Só Será Exibida Caso Atenda a Um Evento.

    litro = float(input("* Quantos kilometros seu veiculo faz com 1 litro de gasolina: "))
        # Nome Da Variável = litro.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    distancia = float(input("* Qual a distancia em kilomentros até o destino: ")) 
        # Nome Da Variável = distancia.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    gasolina_comum = 6.59
        # Atribuindo Um Valor a Variável.

    destino = litro * distancia
        # Nome Da Variável = destino.
        # Função = Calculo De Variáveis.
        # (Valor Da Variável) -> litro * (Valor Da Variável) -> distancia.

    valor = destino * gasolina_comum
        # Nome Da Variável = valor.
        # Função = Calculo De Variáveis.
        # (Valor Da Variável) -> destino * (Valor Da Variável) -> gasolina_Comum.

    print ("-" * 60)

    print ("-Se não Houver Nenhum Imprevisto O Valor até {} é de R${}".format(local, valor))
        # Função = Entrada De Dados.
        # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (gasolina == "Flex") or (gasolina == "flex"):
    # Estrutura De Repetição.
        # Só Será Exibida Caso Atenda a Um Evento.

    litro = float(input("* Quantos kilometros seu veiculo faz com 1 litro de gasolina: "))
        # Nome Da Variável = litro.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    distancia = float(input("* Qual a distancia em kilomentros até o destino: ")) 
        # Nome Da Variável = distancia.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    gasolina_comum = 6.59
        # Atribuindo Um Valor a Variável.

    destino = litro * distancia
        # Nome Da Variável = destino.
        # Função = Calculo De Variáveis.
        # (Valor Da Variável) -> litros * (Valor Da Variável) -> distancia.

    valor = destino * gasolina_comum
        # Nome Da Variável = valor.
        # Função = Calculo De Variáveis.
        # (Valor Da Variável) -> destino * (Valor Da Variável) -> gasolina_comum.

    print ("-" * 60)

    print ("-Se não Houver Nenhum Imprevisto O Valor até {} é de R${} em gasolina.".format(local, valor))
        # Função = Entrada De Dados.
        # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Varivel No Espaço: {}.
            # Ex: .format(Nome_da_Variável).



print ("=" * 60)

print ("*** Fim Do Calculo ***")
    # Função = Entrada De Dados.
    # Apresentando Mensagem Na Tela.

print ("=" * 60)