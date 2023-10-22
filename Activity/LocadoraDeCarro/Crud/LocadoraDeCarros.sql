# codigo para executar no sql

create database locadora_brum;
drop database locadora_brum;

select * from usuario;
select * from veiculo;
select * from veiculoAlugadosDiaria;
select * from alugarVeiculoMensal;
select * from comprarVeiculo;

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

INSERT INTO usuario(nome,cpf,telefone,nasc,senha,pais,cidade,estado)
values
('ArthurBrum','123','67993225188','22072002','123','BR','CG','MS'),
('Augusto','456','67993526161','08102000','456','BR','CG','MS'),
('Fabricia','789','67996838383','789','789','BR','CG','MS');

create table veiculo(
  id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
  marca varchar(255),
  modelo varchar(11),
  cor varchar(11),
  valor_diario varchar(20),
  valor_mensal varchar(255),
  valor_compra varchar(100)
);

INSERT INTO veiculo(marca,modelo,cor,valor_diario,valor_mensal,valor_compra)
values
('Mercedes','V5','Branco','200','2000','2000000'),
('Ferrari','V5','Vermelha','500','5000','5000000'),
('Lamborguini','V5','Preto','800','8000','8000000');

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