import psycopg2

def conexao_banco():
    conexao = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = '12345',
    database = 'LocadoraDeCarros',
    port = '5432'
    )

    print(conexao.info)
    print(conexao.status)


    cursor = conexao.cursor()

    #crud

    cursor.close()
    conexao.close()