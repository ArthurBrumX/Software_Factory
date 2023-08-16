CREATE DATABASE AZMerit;
-- SGBD: PostgreSQL.
-- Sequência para criação das tabelas (pgAdmin4).
-- 03.08.2023
-- A criação das tabelas estão baseadas na moldelagem lógica (Lucidchart).
-- Estes dois traços (--) indicam comentários no script. Eles são “ignorados” e não são interpretados.



-- Tabela 01 - cor marrom esquisito 1OK
CREATE TABLE status_usuario(
	id_status_user SERIAL PRIMARY KEY,
	status BOOL NOT NULL,
	descricao_status_user VARCHAR(70) NOT NULL
);


-- Tabela 02 - cor terracota 2OK
CREATE TABLE status_produto(
	id_status_produto SERIAL PRIMARY KEY,
	disponibilidade BOOL NOT NULL,
	descricao_status_prod VARCHAR(50) NOT NULL
);


-- Tabela 03 - cor áqua 3OK
CREATE TABLE perfil_usuario(
	id_perfil_usuario SERIAL PRIMARY KEY,
	descricao_perfil VARCHAR(50) NOT NULL
);


-- Tabela 04 - cor lilás 4OK 
CREATE TABLE status_feedback(
	id_status_feedback SERIAL PRIMARY KEY,
	status BOOL NOT NULL,
	descricao_feedback VARCHAR(40) NOT NULL
);


-- Tabela 05 - cor rosa 5OK
CREATE TABLE produto(
	id_produto SERIAL PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	imagem VARCHAR,
	descricao VARCHAR(250),
	qde_produto INT,
	valor_produto DECIMAL(20,2) NOT NULL,
	id_status_produto INT,
	FOREIGN KEY (id_status_produto) REFERENCES status_produto(id_status_produto)
);


-- Tabela 09 - cor cinza escuro 6OK
CREATE TABLE usuario(
	id_usuario SERIAL PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	email VARCHAR(150) NOT NULL,
	senha VARCHAR(20) NOT NULL,
	imagem VARCHAR,
	apelido VARCHAR(50),
	id_perfil_usuario INT,
	id_status_user INT,
	FOREIGN KEY (id_perfil_usuario) REFERENCES perfil_usuario(id_perfil_usuario),
	FOREIGN KEY (id_status_user) REFERENCES status_usuario(id_status_user)
);



-- Tabela 06 - cor rosa 7OK
CREATE TABLE campanha(
	id_campanha SERIAL PRIMARY KEY,
	nome_campanha VARCHAR(150) NOT NULL,
	data_inicio DATE DEFAULT NOW() NOT NULL,
	hora_inicio TIME DEFAULT NOW(),
	data_final DATE NOT NULL,
	hora_final TIME,
	saldo_distr DECIMAL(20,2),
	qde_az_por_colaborador DECIMAL(20,2)NOT NULL,
	id_usuario INT,
-- id_carteira INT,
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
-- FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira)
);
-- REMOVIDO A INSTRUÇÃO DE CRIAÇÃO DA FK ID_CARTEIRA PORQUE A TABELA CARTEIRA AINDA NÃO FOI CRIADA
-- Fazer um ALTER TABLE depois para incluí-la.

-- A instrução de alteração será colocada AO FINAL dos blocos de CREATE TABLE



-- Tabela 07 - cor vermelho 8OK
CREATE TABLE estoque(
	id_estoque SERIAL PRIMARY KEY,
	qde_entrada INT NOT NULL,
	qde_total_estoque INT NOT NULL, 
	data_entrada DATE DEFAULT NOW() NOT NULL,
	hora_entrada TIME DEFAULT NOW(),
	custo_prod DECIMAL(20,2)NOT NULL,
	id_produto INT,
	FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);



-- Tabela 12 - cor sem cor 9OK
CREATE TABLE feedback(
	id_feedback SERIAL PRIMARY KEY,
	qde_az_enviado DECIMAL(20,2)NOT NULL,
	data_validacao DATE DEFAULT NOW() NOT NULL,
	hora_validacao TIME DEFAULT NOW() NOT NULL,
	mensagem VARCHAR(240) NOT NULL,
	remetente_usuario INT,
	destinatário_usuario INT,
	id_status_feedback INT,
	id_usuario INT,
	id_campanha INT,
	FOREIGN KEY (id_status_feedback) REFERENCES status_feedback(id_status_feedback),
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
	FOREIGN KEY (id_campanha) REFERENCES campanha(id_campanha)
);


-- Tabela 14 – cor laranja  10OK
CREATE TABLE tipo_saida(
	id_tipo_saida SERIAL PRIMARY KEY,
	qde_saida INT,
	justificativa VARCHAR(150),
	data_saida DATE DEFAULT NOW(),
	hora_saida TIME DEFAULT NOW(),
	id_produto INT,
	id_estoque INT,
	id_usuario INT,
	FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
	FOREIGN KEY (id_estoque) REFERENCES estoque(id_estoque),
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);




-- Tabela 13 - cor amarelo 11OK
CREATE TABLE analise(
	id_analise SERIAL PRIMARY KEY,
	qde_enviado DECIMAL(20,2),
	data_analise DATE DEFAULT NOW() NOT NULL,
	hora_analise TIME DEFAULT NOW() NOT NULL,
	mensagem VARCHAR(240),
	id_feedback INT,
	id_status_feedback INT,
--	id_carteira INT,
	FOREIGN KEY (id_feedback) REFERENCES feedback(id_feedback),
	FOREIGN KEY (id_status_feedback) REFERENCES status_feedback(id_status_feedback)
--    FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira_nao_usar)
);

-- REMOVIDO A INSTRUÇÃO DE CRIAÇÃO DA FK ID_CARTEIRA PORQUE A TABELA CARTEIRA AINDA NÃO FOI CRIADA
-- Fazer um ALTER TABLE depois para incluí-la.

-- A instrução de alteração será colocada AO FINAL dos blocos de CREATE TABLE

-- Tabela 11 - cor azul claro 12OK
-- Atenção: TABELA CARTEIRA ainda não foi criada
-- REMOVIDO A INSTRUÇÃO DE CRIAÇÃO DA FK ID_CARTEIRA PORQUE A TABELA CARTEIRA AINDA NÃO FOI CRIADA
-- REMOVIDO A INSTRUÇÃO DA CRIAÇÃO DA COLUNA id_cateira INT
-- Fazer um ALTER TABLE depois para incluí-la.
CREATE TABLE troca_produto(
	id_troca_produto SERIAL PRIMARY KEY,
	qde_troca_produto INT NOT NULL,
	data_troca_prod DATE DEFAULT NOW(),
	hora_troca_prod TIME DEFAULT NOW(),
--	id_carteira INT,
	id_produto INT,
--	FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira_nao_usar),
	FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

-- A instrução de alteração será colocada ao final do bloco de instruções CREATE TABLE e junto aos ALTER TABLE





-- Tabela 10 – cor verde claro  13OK
-- Criar esta tabela antes das tabelas Campanha e Troca
-- REMOVIDO A INSTRUÇÃO DE CRIAÇÃO DA FK ID_CARTEIRA PORQUE A TABELA CARTEIRA AINDA NÃO FOI CRIADA
-- REMOVIDO A INSTRUÇÃO DA CRIAÇÃO DA COLUNA id_cateira INT
-- Fazer um ALTER TABLE depois para incluí-la.
CREATE TABLE tipo_transacao(
	id_tipo_transacao SERIAL PRIMARY KEY,
--	id_carteira INT,
	id_troca_produto INT,
--	FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira_nao_usar),
	FOREIGN KEY (id_troca_produto) REFERENCES troca_produto(id_troca_produto)
);


-- A instrução de alteração será colocada ao final do bloco de instruções CREATE TABLE e junto aos ALTER TABLE



-- Tabela 08 - cor verde pistache 14OK
CREATE TABLE central_transacao(
	id_central_transacao SERIAL PRIMARY KEY,
	saldo_total_mov DECIMAL(20,2),	
	valor_enviado DECIMAL(20,2),
	valor_recebido DECIMAL(20,2),
	id_tipo_transacao INT,
	FOREIGN KEY (id_tipo_transacao) REFERENCES tipo_transacao(id_tipo_transacao)
);



-- Tabela 15 – cor bege  15OK
CREATE TABLE carteira(
	id_carteira SERIAL PRIMARY KEY,
	valor_recebido_campanha DECIMAL(20,2),
	saldo_doacao_usuario DECIMAL(20,2),
	saldo_recebido_feedback DECIMAL(20,2),
	saldo_pendente_aprovacao DECIMAL(20,2),
	id_usuario INT,
	id_campanha INT,
	id_analise INT,
	id_central_transacao INT,
	id_status_feedback INT,
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
	FOREIGN KEY (id_campanha) REFERENCES campanha(id_campanha),
	FOREIGN KEY (id_analise) REFERENCES analise(id_analise),
	FOREIGN KEY (id_central_transacao) REFERENCES central_transacao(id_central_transacao),
	FOREIGN KEY (id_status_feedback) REFERENCES status_feedback(id_status_feedback)
);

-- ------------------------------------------------------------------------------------------------
-- Estas instruções são complementares e obrigatórios para a inclusão das chaves estrangeiras nas tabelas

-- Tabela 06 - cor rosa 7OK
ALTER TABLE campanha
ADD COLUMN id_carteira INT,
ADD CONSTRAINT id_carteira FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira);

-- Tabela 13 - cor amarelo 11OK
ALTER TABLE analise
ADD COLUMN id_carteira INT,
ADD CONSTRAINT id_carteira FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira);

-- Tabela 11 - cor azul claro 12OK
ALTER TABLE troca_produto
ADD COLUMN id_carteira int,
ADD CONSTRAINT id_carteira FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira);

-- Tabela 10 – cor verde claro  13OK
ALTER TABLE tipo_transacao
ADD COLUMN id_carteira int,
ADD CONSTRAINT id_carteira FOREIGN KEY (id_carteira) REFERENCES carteira(id_carteira);


-- ------------------------------------------------------------------------------------------------

SELECT * FROM analise;
SELECT * FROM campanha;
SELECT * FROM carteira;
SELECT * FROM central_transacao;
SELECT * FROM estoque;
SELECT * FROM feedback;
SELECT * FROM perfil_usuario;
SELECT * FROM produto;
SELECT * FROM status_feedback;
SELECT * FROM status_produto;
SELECT * FROM status_usuario;
SELECT * FROM tipo_saida;
SELECT * FROM tipo_transacao;
SELECT * FROM troca_produto;
SELECT * FROM usuario;
