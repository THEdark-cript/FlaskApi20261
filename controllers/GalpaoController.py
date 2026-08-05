from flask import Blueprint, request, jsonify
import psycopg2
from marshmallow import ValidationError

from Service.GalpoesService import GalpaoService
from models.Galpao import GalpaoSchema
from helpers.logger import logger

galpao_bp = Blueprint('galpao', __name__, url_prefix='/galpoes')
service = GalpaoService()

@galpao_bp.get("/")
def getGalpoes():
    logger.info("Controller: Listando todos os galpões")
    try:
        galpoes = service.getAllGalpoes()
        return jsonify([g.toDict() for g in galpoes]), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao listar galpões"}, 500

@galpao_bp.get("/<int:id>")
def getByIdGalpao(id: int):
    logger.info(f"Controller: Buscando galpão pelo id: {id}")
    try:
        galpao = service.getByIdGalpao(id)
        if galpao is None:
            return {"mensagem": "Galpão não encontrado"}, 404
        return galpao.toDict(), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao buscar galpão"}, 500

@galpao_bp.post("/")
def postGalpao():
    try:
        dados = request.get_json()
        schema = GalpaoSchema()
        dados_validados = schema.load(dados)

        id = service.criarGalpao(dados_validados)
        return {"mensagem": "Galpão criado com sucesso!", "id": id}, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao criar galpão"}, 500

@galpao_bp.put("/<int:id>")
def putGalpao(id: int):
    try:
        dados = request.get_json()
        schema = GalpaoSchema()
        dados_validados = schema.load(dados)

        linhas = service.atualizarGalpao(id, dados_validados)
        if linhas == 0:
            return {"mensagem": "Galpão não encontrado"}, 404
        return {"mensagem": "Galpão atualizado com sucesso"}, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao atualizar galpão"}, 500

@galpao_bp.delete("/<int:id>")
def deleteGalpao(id: int):
    logger.info(f"Controller: Deletando galpão id: {id}")
    try:
        linhas = service.deletarGalpao(id)
        if linhas == 0:
            return {"mensagem": "Galpão não encontrado"}, 404
        return {"mensagem": "Galpão removido com sucesso!"}, 202
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno ao remover galpão"}, 500
