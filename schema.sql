CREATE TABLE IF NOT EXISTS tb_avicultor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_avicola (
    id SERIAL PRIMARY KEY,
     endereco TEXT NOT NULL,
    territorio TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_galpao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    capacidade INTEGER NOT NULL,
     tipo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_aviario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    capacidade INTEGER NOT NULL
);
