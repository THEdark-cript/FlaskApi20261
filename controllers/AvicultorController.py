from flask import Blueprint
import sqlite3
from flask import request, jsonify
from marshmallow import ValidationError

from models.Avicultor import Avicultor, AvicultorSchema
from service.AvicultoresService import AvicultorService
from helpers.database import get_conn
from helpers.logger import logger

# 'auth' is the blueprint name; __name__ helps Flask locate resources
avicultor_bp = Blueprint('avicultor', __name__, url_prefix='/avicultores')


@avicultor_bp.route('/<int:id>')
def getByIdAvicultores(id: int):
    logger.info(f"Listando avicultores pelo id: {id}")
    avicultor = None
    try:
        logger.info("Abrindo a conexão com o banco")

        avicultorService = AvicultorService()
        avicultor = avicultorService.getByIdAvicultor(id)

        if avicultor is None:
            return {"mensagem": "O avicultor não foi encontrado"}, 404

    except sqlite3.Error as e:
        logger.error(e)

    return avicultor.toDict(), 200


@avicultor_bp.get("/")
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


@avicultor_bp.post("/")
def postAvicultores():
    avicultorJson = request.get_json()
    # DB
    conn = None
    try:
        avicultorSchema = AvicultorSchema()
        avicultorData = avicultorSchema.load(avicultorJson)

        # 1 - Abrir a conexão
        conn = get_conn()

        # 2 - Recuperar o cursor
        cursor = conn.cursor()

        # 3 - Preparar a consultar: query | statement
        cursor.execute(
            "INSERT INTO tb_avicultores(nome, nascimento, cpf, caf) VALUES(?, ?, ?, ?)", (avicultorData["nome"], avicultorData["nascimento"], avicultorData["cpf"], avicultorData["caf"]))

        id = cursor.lastrowid
        avicultorData["id"] = id

        # 4.2 - Confirmar operação.
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    except ValidationError as err:
        return jsonify(err.messages), 400
    finally:
        # 5 - Fechar a conexão
        if conn:
            conn.close()

    return avicultorData, 200


@avicultor_bp.put("/")
def putAvicultores():
    pass


@avicultor_bp.delete("/<int:id>")
def deleteAvicultores(id: int):
    try:
        conn = get_conn()
        # 2 - Recuperar o cursor
        cursor = conn.cursor()
        # Antes de remover verificar se existe, caso não existe enviar mensagem de entidade não existente
        # 3 - Preparar a consultar: query | statement
        stmt = "delete from tb_avicultores where id=?"
        cursor.execute(stmt, (id, ))
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    return {"mensagem": "Avicultor removido com sucesso!"}, 202

# /avicultores - nome, cpf, caf, nascimento
# /avicolas
# /aviarios ou /galpoes