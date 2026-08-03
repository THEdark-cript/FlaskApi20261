from flask import Blueprint, request, jsonify
from services.aviario_service import AviarioService
from helpers.logger import logger

aviario_bp = Blueprint('aviario', __name__, url_prefix='/aviarios')
service = AviarioService()

@aviario_bp.get("/")
def getAviarios():
    aviarios = service.listar()
    return jsonify([a.toDict() for a in aviarios]), 200

@aviario_bp.get("/<int:id>")
def getAviario(id):
    aviario = service.buscar(id)
    if aviario is None:
        return {"mensagem": "Aviário não encontrado"}, 404
    return aviario.toDict(), 200

@aviario_bp.post("/")
def postAviario():
    dados = request.get_json()
    try:
        id = service.criar(dados)
        return {"mensagem": "Aviário criado com sucesso!", "id": id}, 201
    except Exception as e:
        logger.error(e)
        return {"mensagem": "Erro ao criar aviário"}, 500

@aviario_bp.put("/<int:id>")
def putAviario(id):
    dados = request.get_json()
    linhas = service.atualizar(id, dados)
    if linhas == 0:
        return {"mensagem": "Aviário não encontrado"}, 404
    return {"mensagem": "Aviário atualizado com sucesso"}, 200

@aviario_bp.delete("/<int:id>")
def deleteAviario(id):
    linhas = service.remover(id)
    if linhas == 0:
        return {"mensagem": "Aviário não encontrado"}, 404
    return {"mensagem": "Aviário removido com sucesso"}, 202
