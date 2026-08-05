from helpers.logger import logger
from Repository.AvicolaRepository import AvicolaRepository
from models.Avicola import Avicola

class AvicolaService():
    def __init__(self):
        self.avicolaRepository = AvicolaRepository()

    def getByIdAvicola(self, id):
        row = self.avicolaRepository.getById(id)
        logger.info("Service: Lendo informações do resultado da consulta ao banco.")
        if row is not None:
            return Avicola(row[0], row[1], row[2])  # id, endereco, territorio
        return None

    def getAllAvicolas(self):
        rows = self.avicolaRepository.getAll()
        avicolas = []
        for row in rows:
            avicola = Avicola(row[0], row[1], row[2])
            avicolas.append(avicola)
        return avicolas

    def criarAvicola(self, dados):
        id = self.avicolaRepository.insert(dados["endereco"], dados["territorio"])
        return id

    def atualizarAvicola(self, id, dados):
        linhas = self.avicolaRepository.update(id, dados["endereco"], dados["territorio"])
        return linhas

    def removerAvicola(self, id):
        linhas = self.avicolaRepository.delete(id)
        return linhas
