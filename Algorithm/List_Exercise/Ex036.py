# 36 - O cardápio da lanchonete Burgão é o seguinte:

# ESPECIFICAÇÃO CÓDIGO PREÇO

# Cachorro Quente       100         R$ 11,20
# Ovo Simples           101         R$ 8,30
# Bauru com Ovo         102         R$ 11,50
# Hambúrguer            103         R$ 16,20
# Refrigerante          201         R$ 6,00
# Suco                  202         R$ 7,50
# Água Mineral          203         R$ 4,70

# Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente.

# Assumaas entradas corretas:

print ("=" * 60)

print ("*** Lanchonete Burgão ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

cachorro_quente = 11.20
    # Nome Da Variável = cachorro_quente.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

ovo_simples = 8.30
    # Nome Da Variável = ovo_simples.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

bauru_com_ovo = 11.50
    # Nome Da Variável = bauru_com_ovo.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

hamburguer = 16.20
    # Nome Da Variável = hamburger.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

refrigerante = 6.0
    # Nome Da Variável = refrigerante.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

suco = 7.50
    # Nome Da Variável = suco.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

agua_mineral = 4.70
    # Nome Da Variável = agua_mineral.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

carrinho = 0
    # Nome Da Variável = carrinho.
    # Tipo Da Variavel = Float (Real).
    # Função = Atribuição De Valor.

print ("=" * 60)

print ("Cachorro Quente --> Código Do Produto: [100]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("Ovo Simples     --> Código Do Produto: [101]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("Bauru Com Ovo   --> Código Do Produto: [102]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("Hamburger       --> Código Do Produto: [103]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("Refrigerante    --> Código Do Produto: [201]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("Suco            --> Código Do Produto: [202]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("Agua Mineral    --> Código Do Produto: [203]")
    # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)

resposta = input("* Deseja fazer o Pedido [S/N]: ")
    # Nome Da Variável = Resposta.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

while (resposta == "Sim") or (resposta == "sim"):
    # While = Enquanto
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.   

    
    codigo = input("* Digite o código do produto: ")
        # Nome Da Variável = codigo.
        # Tipo Da Variável = Str (String).
        # Função = Entrada De Dados.

    if (codigo == "100"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + cachorro_quente
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> cachorro_quente.

        print ("+ 1 cachorro quente")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    if (codigo == "101"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + ovo_simples
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> ovo_simples.

        print ("+ 1 Ovo Simples")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    if (codigo == "102"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + bauru_com_ovo
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> bauru_com_ovo.

        print ("+ 1 Bauru Com Ovo")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    if (codigo == "103"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + hamburguer
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> hamburger.

        print ("+ 1 Hamburger")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    if (codigo == "201"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + refrigerante
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> refrigerante.

        print ("+ 1 Refrigerante")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    if (codigo == "202"):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + suco
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> suco.

        print ("+ 1 Suco")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    if (codigo == "203"):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        carrinho = carrinho + agua_mineral
            # Nome Da Variável = carrinho.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> carrinho + (Valor Da Variável: ) -> agua_mineral.

        print ("+ 1 Agua Mineral")
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.

    resposta = input("* Deseja continuar o Pedido: ")
        # Nome Da Variável = Resposta.
        # Tipo Da Variável = Str (String).
        # Função = Entrada De Dados.
        
else:
    print ("- A conta deu no total de R$ {}!".format(carrinho))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)

