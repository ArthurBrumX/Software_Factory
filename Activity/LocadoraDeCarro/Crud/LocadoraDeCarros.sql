create table clientes(
id_usuario serial primary key,
nome varchar(100) not null,
cpf float(11) not null,
telefone varchar(11) not null,
data_Nasc date,
senha_Acess varchar(150) not null
);

create table carros(
id_carro serial primary key,
marca varchar(100) not null,
modelo varchar(100) not null,
cor varchar(100) not null,
valor_diario float(50) not null,
valor_mensal float(50) not null,
valor_compra float(50) not null
);


