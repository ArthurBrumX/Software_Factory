# 67 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print ("=" * 60)

print ("*** Login De Usuário!! ***")
    # Boas-Vindas Ao Usuario.

print ("*** Sejá Bem-Vindo! ***")
    # Apresentação Ao Usuário.

print ("=" * 60)

usuario = input("* Digite Seu Nome: ")
    # Nome Da Variável = usuario.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

senha = (input("* Digite Sua Senha De Acesso: "))
    # Nome Da Variável = senha.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

while (senha == usuario):
    # While = Enquanto
        # Enquanto Essa Condição For Verdadeira Execute o Código a Baixo.

    print("* A senha Não pode Ser Igual ao seu nome de Usuario!! \n")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

    usuario = input("- Digite Seu Nome: ")
        # Nome Da Variável = usuario.
        # Tipo Da Variável = Str (String).
        # Função = Entrada De Dados.

    senha = (input("- Digite Sua Senha De Acesso: "))
        # Nome Da Variável = senha.
        # Tipo Da Variável = Str (String).
        # Função = Entrada De Dados.

print ("- Senha Aceita Com Sucesso, Bem-Vindo {}".format(usuario))
    # Função = Saída De Dados.
    # Apresentando Mensagem Na Tela.
    # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
        # Ex: .format(Nome_da_Variável).


print ("=" * 60)






