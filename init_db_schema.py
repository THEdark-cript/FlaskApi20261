import sqlite3

DATABASE_NAME = "avicola.db"

conn = None
try:
    #1- abrir a conexão
    conn = sqlite3.connect(DATABASE_NAME)

    #2- recuperar o cursor
    cursor = conn.cursor()

    #3- preparar a consulta: query statement
    with open('schema.sql', mode='r') as file:
        cursor.executescript(file.read())

    #4.1- iterar nos resultados:
    #4.2- confirmar alterações:
    conn.commit()
except sqlite3.Error as e:
    print(e)
finally:
    #5- fechar a conexão
    if conn:
        conn.close()