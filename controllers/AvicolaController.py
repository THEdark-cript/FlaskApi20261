from flask import Blueprint, request, jsonify
import sqlite3
from marshmallow import ValidationError

from models.Avicola import Avicola, AvicolaSchema
from services.AvicolaService import AvicolaService
from helpers.database import get_conn
from helpers.logger import logger

# Blueprint para Avícolas
avicola_bp = Blueprint('avicola', __name__, url_prefix='/avicolas')


@avicola_bp.route('/<int:id>')
def getByIdAvicola(id: int):
    logger.info(f"Buscando avícola pelo id: {id}")
    try:
        avicolaService = AvicolaService()
        avicola = avicolaService.getByIdAvicola(id)

        if avicola is None:
            return {"mensagem": "Avícola não encontrada"}, 404

        return avicola.toDict(), 200
    except sqlite3.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao buscar avícola"}, 500


@avicola_bp.get("/")
def getAvicolas():
    try:
        avicolaService = AvicolaService()
        avicolas = avicolaService.getAvicolas()
        return jsonify([a.toDict() for a in avicolas]), 200
    except sqlite3.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao listar avícolas"}, 500


@avicola_bp.post("/")
def postAvicola():
    dados = request.get_json()
    try:
        schema = AvicolaSchema()
        dados_validados = schema.load(dados)

        avicolaService = AvicolaService()
        id = avicolaService.criarAvicola(dados_validados)

        return {"mensagem": "Avícola criada com sucesso!", "id": id}, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except sqlite3.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao criar avícola"}, 500


@avicola_bp.put("/<int:id>")
def putAvicola(id: int):
    dados = request.get_json()
    try:
        schema = AvicolaSchema()
        dados_validados = schema.load(dados)

        avicolaService = AvicolaService()
        linhas = avicolaService.atualizarAvicola(id, dados_validados)

        if linhas == 0:
            return {"mensagem": "Avícola não encontrada"}, 404
        return {"mensagem": "Avícola atualizada com sucesso"}, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except sqlite3.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao atualizar avícola"}, 500


@avicola_bp.delete("/<int:id>")
def deleteAvicola(id: int):
    try:
        avicolaService = AvicolaService()
        linhas = avicolaService.removerAvicola(id)

        if linhas == 0:
            return {"mensagem": "Avícola não encontrada"}, 404
        return {"mensagem": "Avícola removida com sucesso!"}, 202
    except sqlite3.Error as e:
        logger.error(e)
        return {"mensagem": "Erro interno ao remover avícola"}, 500
