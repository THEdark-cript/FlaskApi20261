from flask import Blueprint, request, jsonify
import psycopg2
from marshmallow import ValidationError

from models.Avicultor import  AvicultorSchema
from Service.AvicultorService import AvicultorService
from helpers.logger import logger

avicultor_bp = Blueprint('avicultor', __name__, url_prefix='/avicultores')
avicultorService = AvicultorService()

@avicultor_bp.get("/<int:id>")
def getByIdAvicultores(id: int):
    logger.info(f"Controller: Buscando avicultor pelo id: {id}")
    try:
        avicultor = avicultorService.getByIdAvicultor(id)
        if avicultor is None:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return avicultor.toDict(), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno no banco de dados"}, 500

@avicultor_bp.get("/")
def getAvicultores():
    logger.info("Controller: Listando todos os avicultores")
    try:
        avicultores = avicultorService.getAllAvicultores()
        return jsonify(avicultores), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno no banco de dados"}, 500

@avicultor_bp.post("/")
def postAvicultores():
    try:
        avicultorJson = request.get_json()
        schema = AvicultorSchema()
        dados_validados = schema.load(avicultorJson)

        resultado = avicultorService.criarAvicultor(dados_validados)
        return jsonify(resultado), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno no banco de dados"}, 500

@avicultor_bp.put("/<int:id>")
def putAvicultores(id: int):
    try:
        avicultorJson = request.get_json()
        schema = AvicultorSchema()
        dados_validados = schema.load(avicultorJson)

        resultado = avicultorService.atualizarAvicultor(id, dados_validados)
        if resultado is None:
            return {"erro": "Avicultor não encontrado."}, 404
        return jsonify(resultado), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno no banco de dados"}, 500

@avicultor_bp.delete("/<int:id>")
def deleteAvicultores(id: int):
    logger.info(f"Controller: Deletando avicultor id: {id}")
    try:
        resultado = avicultorService.deletarAvicultor(id)
        if resultado is None:
            return {"mensagem": "Não foi possível remover: O avicultor informado não existe no sistema."}, 404
        return jsonify(resultado), 202
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno no banco de dados"}, 500
