# codigo para executar no sql

# select *  from usuario;
# select *  from veiculo;


create database locadora_brum;
use locadora_brum;
create table usuario(
	nome varchar(255),
    cpf varchar(11),
    telefone varchar(11),
    nasc varchar(20),
    senha varchar(255),
    pais varchar(100),
    cidade varchar(255),
    estado varchar(255)
);
 
create table veiculo(
  marca varchar(255),
  modelo varchar(11),
  cor varchar(11),
  valor_diario varchar(20),
  valor_mensal varchar(255),
  valor_compra varchar(100)
);