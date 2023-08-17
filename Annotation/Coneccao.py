#Primeiros passo: Importar as Bibliotecas
import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

#Segundo passo: Atribuir em uma variavel a String de conecção 
engine = create_engine("postgresql://postgres:12345@localhost:5432/atendimentos")

#Terceiro passo: Criar a conecçao do pgadmin
connection = pg.connect(user="postgres",password="12345",host="localhost",port="5432",database="atendimentos")
curs=connection.cursor

#Quarto passo: Atribuir os comandos
sql = "SELECT nome, cpf, telefone, atendido ,ddd FROM clientes"
df = pd.read_sql_query(sql, con=engine)
print(df)

#sql_insert="INSERT INTO Usuarios (nome,email,senha) Values ('pedro','pedro@gmail.com','senha1234')"
#curs.execute(sql_insert)
#connection.commit()

#sql_update "UPDATE usuarios SET nome = 'maria' WHERE id = 2"
#curs.execute(sql_update)
#connection.commit()

