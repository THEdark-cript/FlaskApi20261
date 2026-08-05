from flask import Blueprint, request, jsonify
import psycopg2
from marshmallow import ValidationError

from models.Aviario import AviarioSchema
from Service.AviarioService import AviarioService
from helpers.logger import logger

aviario_bp = Blueprint('aviario', __name__, url_prefix='/aviarios')
service = AviarioService()

@aviario_bp.get("/")
def getAviarios():
    logger.info("Controller: Listando todos os aviários")
    try:
        aviarios = service.getAllAviarios()
        return jsonify([a.toDict() for a in aviarios]), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao listar aviários"}, 500

@aviario_bp.get("/<int:id>")
def getByIdAviario(id: int):
    logger.info(f"Controller: Buscando aviário pelo id: {id}")
    try:
        aviario = service.getByIdAviario(id)
        if aviario is None:
            return {"mensagem": "Aviário não encontrado"}, 404
        return aviario.toDict(), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao buscar aviário"}, 500

@aviario_bp.post("/")
def postAviario():
    try:
        dados = request.get_json()
        schema = AviarioSchema()
        dados_validados = schema.load(dados)

        id = service.criarAviario(dados_validados)
        return {"mensagem": "Aviário criado com sucesso!", "id": id}, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao criar aviário"}, 500

@aviario_bp.put("/<int:id>")
def putAviario(id: int):
    try:
        dados = request.get_json()
        schema = AviarioSchema()
        dados_validados = schema.load(dados)

        linhas = service.atualizarAviario(id, dados_validados)
        if linhas == 0:
            return {"mensagem": "Aviário não encontrado"}, 404
        return {"mensagem": "Aviário atualizado com sucesso"}, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao atualizar aviário"}, 500

@aviario_bp.delete("/<int:id>")
def deleteAviario(id: int):
    logger.info(f"Controller: Deletando aviário id: {id}")
    try:
        linhas = service.removerAviario(id)
        if linhas == 0:
            return {"mensagem": "Aviário não encontrado"}, 404
        return {"mensagem": "Aviário removido com sucesso!"}, 202
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao remover aviário"}, 500
