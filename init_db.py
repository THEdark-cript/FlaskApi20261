import sqlite3

DATABASE_NAME = 'avicola.db'

tables = [
    """CREATE TABLE IF NOT EXISTS avicultores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
    )"""
]

conn = None
try:
    #1- abrir a conexão
    conn = sqlite3.connect(DATABASE_NAME)

    #2- recuperar o cursor
    cursor = conn.cursor()

    #3- preparar a consulta: query statement
    for table in tables:
        cursor.execute(table)

    #4.1- iterar nos resultados:
    #4.2- confirmar alterações:
    conn.commit()
except sqlite3.Error as e:
    print(e)
finally:
    #5- fechar a conexão
    if conn:
        conn.close()