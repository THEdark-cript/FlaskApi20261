from flask import Blueprint, request, jsonify
import psycopg2
from marshmallow import ValidationError

from models.Avicola import AvicolaSchema
from Service.AvicolaService import AvicolaService
from helpers.logger import logger

avicola_bp = Blueprint('avicola', __name__, url_prefix='/avicolas')
service = AvicolaService()

@avicola_bp.get("/")
def getAvicolas():
    logger.info("Controller: Listando todas as avícolas")
    try:
        avicolas = service.getAllAvicolas()
        return jsonify([a.toDict() for a in avicolas]), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao listar avícolas"}, 500

@avicola_bp.get("/<int:id>")
def getByIdAvicola(id: int):
    logger.info(f"Controller: Buscando avícola pelo id: {id}")
    try:
        avicola = service.getByIdAvicola(id)
        if avicola is None:
            return {"mensagem": "Avícola não encontrada"}, 404
        return avicola.toDict(), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao buscar avícola"}, 500

@avicola_bp.post("/")
def postAvicola():
    try:
        dados = request.get_json()
        schema = AvicolaSchema()
        dados_validados = schema.load(dados)

        id = service.criarAvicola(dados_validados)
        return {"mensagem": "Avícola criada com sucesso!", "id": id}, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao criar avícola"}, 500

@avicola_bp.put("/<int:id>")
def putAvicola(id: int):
    try:
        dados = request.get_json()
        schema = AvicolaSchema()
        dados_validados = schema.load(dados)

        linhas = service.atualizarAvicola(id, dados_validados)
        if linhas == 0:
            return {"mensagem": "Avícola não encontrada"}, 404
        return {"mensagem": "Avícola atualizada com sucesso"}, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao atualizar avícola"}, 500

@avicola_bp.delete("/<int:id>")
def deleteAvicola(id: int):
    logger.info(f"Controller: Deletando avícola id: {id}")
    try:
        linhas = service.removerAvicola(id)
        if linhas == 0:
            return {"mensagem": "Avícola não encontrada"}, 404
        return {"mensagem": "Avícola removida com sucesso!"}, 202
    except psycopg2.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao remover avícola"}, 500
