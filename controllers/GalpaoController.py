from flask import Blueprint, request, jsonify
from services.galpao_service import GalpaoService
from helpers.logger import logger

galpao_bp = Blueprint('galpao', __name__, url_prefix='/galpoes')
service = GalpaoService()

@galpao_bp.get("/")
def getGalpoes():
    galpoes = service.listar()
    return jsonify([g.toDict() for g in galpoes]), 200

@galpao_bp.get("/<int:id>")
def getGalpao(id):
    galpao = service.buscar(id)
    if galpao is None:
        return {"mensagem": "Galpão não encontrado"}, 404
    return galpao.toDict(), 200

@galpao_bp.post("/")
def postGalpao():
    dados = request.get_json()
    try:
        id = service.criar(dados)
        return {"mensagem": "Galpão criado com sucesso!", "id": id}, 201
    except Exception as e:
        logger.error(e)
        return {"mensagem": "Erro ao criar galpão"}, 500

@galpao_bp.put("/<int:id>")
def putGalpao(id):
    dados = request.get_json()
    linhas = service.atualizar(id, dados)
    if linhas == 0:
        return {"mensagem": "Galpão não encontrado"}, 404
    return {"mensagem": "Galpão atualizado com sucesso"}, 200

@galpao_bp.delete("/<int:id>")
def deleteGalpao(id):
    linhas = service.remover(id)
    if linhas == 0:
        return {"mensagem": "Galpão não encontrado"}, 404
    return {"mensagem": "Galpão removido com sucesso"}, 202
