from helpers.logger import logger
from Repository.GalpoesRepository import GalpaoRepository
from models.Galpao import Galpao

class GalpaoService():
    def __init__(self):
        self.galpaoRepository = GalpaoRepository()

    def getByIdGalpao(self, id):
        row = self.galpaoRepository.getById(id)
        logger.info("Service: Lendo informações do resultado da consulta ao banco.")
        if row is not None:
            return Galpao(row[0], row[1], row[2], row[3])  # id, nome, capacidade, tipo
        return None

    def getAllGalpoes(self):
        rows = self.galpaoRepository.getAll()
        galpoes = []
        for row in rows:
            galpao = Galpao(row[0], row[1], row[2], row[3])
            galpoes.append(galpao)
        return galpoes

    def criarGalpao(self, dados):
        id = self.galpaoRepository.insert(dados["nome"], dados["capacidade"], dados["tipo"])
        return id

    def atualizarGalpao(self, id, dados):
        linhas = self.galpaoRepository.update(id, dados["nome"], dados["capacidade"], dados["tipo"])
        return linhas

    def deletarGalpao(self, id):
        linhas = self.galpaoRepository.delete(id)
        return linhas
