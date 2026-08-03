CREATE TABLE IF NOT EXISTS tb_avicultores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_avicolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    capacidade INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_galpoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    capacidade INTEGER NOT NULL,
    avicola_id INTEGER,
    FOREIGN KEY (avicola_id) REFERENCES tb_avicolas(id)
);

CREATE TABLE IF NOT EXISTS tb_aviarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    capacidade INTEGER NOT NULL,
    galpao_id INTEGER,
    FOREIGN KEY (galpao_id) REFERENCES tb_galpoes(id)
);
