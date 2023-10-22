# codigo para executar no sql

create database locadora_brum;
drop database locadora_brum;

select *  from usuario;
select *  from veiculo;

use locadora_brum;

create table usuario(
	id_usuario INT AUTO_INCREMENT PRIMARY KEY,
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
  id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
  marca varchar(255),
  modelo varchar(11),
  cor varchar(11),
  valor_diario varchar(20),
  valor_mensal varchar(255),
  valor_compra varchar(100)
);

create table veiculoAlugadosDiaria(
  id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
  marca varchar(255),
  modelo varchar(11),
  cor varchar(11),
  valor_diario varchar(20),
  valor_mensal varchar(255),
  valor_compra varchar(100)
);

create table alugarVeiculoMensal(
	id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
  marca varchar(255),
  modelo varchar(11),
  cor varchar(11),
  valor_diario varchar(20),
  valor_mensal varchar(255),
  valor_compra varchar(100)
);

create table comprarVeiculo(
	id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
  marca varchar(255),
  modelo varchar(11),
  cor varchar(11),
  valor_diario varchar(20),
  valor_mensal varchar(255),
  valor_compra varchar(100)
);