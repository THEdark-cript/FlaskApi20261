from flask import Flask, jsonify, request
import sqlite3

from models.Avicultor import Avicultor
from helpers.application import app
from helpers.database import get_conn

@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200


@app.get("/avicultores")
def getAvicultores():

    avicultores = []

    # DB
    conn = None
    try:
        
        conn = get_conn()
        # 2 - Recuperar o cursor
        cursor = conn.cursor()

        # 3 - Preparar a consultar: query | statement
        cursor.execute("select * from tb_avicultores")

        # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
        rows = cursor.fetchall()

        for row in rows:
            id = row[0]
            nome = row[1]
            nascimento = row[2]
            cpf = row[3]
            caf = row[4]
            avicultor = Avicultor(id, nome, nascimento, cpf, caf)
            avicultores.append(avicultor.toDict())

    except sqlite3.Error as e:
        print(e)
    finally:
        # 5 - Fechar a conexão
        if conn:
            conn.close()

    return avicultores, 200


@app.post("/avicultores")
def postAvicultores():
    avicultorJson = request.get_json()
    # DB
    conn = None
    try:
        conn = get_conn()
        # 2 - Recuperar o cursor
        cursor = conn.cursor()

        # 3 - Preparar a consulta: query | statement
        cursor.execute(
            "INSERT INTO tb_avicultores (nome, nascimento, cpf, caf) VALUES (?, ?, ?, ?)",
            (avicultorJson["nome"], avicultorJson["nascimento"], avicultorJson["cpf"], avicultorJson["caf"])
        )
        conn.commit()

    except sqlite3.Error as e:
        print(e)
    finally:
        # 5 - Fechar a conexão
        if conn:
            conn.close()

    return avicultorJson, 201


@app.put("/avicultores/<cpf>")
def putAvicultores(cpf):
    requisicao = request.get_json()
    # DB
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE tb_avicultores SET nome=?, nascimento=?, caf=? WHERE cpf=?",
            (requisicao["nome"], requisicao["nascimento"], requisicao["caf"], cpf)
        )
        conn.commit()

    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    return {"mensagem": "Avicultor atualizado com sucesso"}, 200


@app.delete("/avicultores/<cpf>")
def deleteAvicultores(cpf):
    # DB
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tb_avicultores WHERE cpf = ?", (cpf,))
        conn.commit()

    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    return {"mensagem": "Avicultor deletado com sucesso"}, 200

# /avicultores - nome, cpf, caf, nascimento
# /avicolas
# /aviarios ou /galpoes
