from helpers.logger import logger
from Repository.AviarioRepository import AviarioRepository
from models.Aviario import Aviario

class AviarioService:
    def __init__(self):
        self.aviarioRepository = AviarioRepository()

    def getByIdAviario(self, id: int):
        row = self.aviarioRepository.getById(id)
        logger.info("Service: Lendo informações do resultado da consulta ao banco.")
        if row is not None:
            return Aviario(row[0], row[1], row[2])  # id, nome, capacidade
        return None

    def getAllAviarios(self):
        rows = self.aviarioRepository.getAll()
        aviarios = []
        for row in rows:
            aviario = Aviario(row[0], row[1], row[2])
            aviarios.append(aviario)
        return aviarios

    def criarAviario(self, dados):
        id = self.aviarioRepository.insert(
            dados["nome"], dados["capacidade"]
        )
        return id

    def atualizarAviario(self, id, dados):
        linhas = self.aviarioRepository.update(
            id, dados["nome"], dados["capacidade"]
        )
        return linhas

    def removerAviario(self, id):
        linhas = self.aviarioRepository.delete(id)
        return linhas
