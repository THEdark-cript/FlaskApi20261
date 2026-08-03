from helpers.logger import logger
from Repository.AvicultorRepository import AvicultorRepository
from models.Avicultor import Avicultor
# Manipulação da regra de negócio


class AvicultorService():
    def __init__(self):
        self.avicultorRepository = AvicultorRepository()

    def getByIdAvicultor(self, id):
        avicultor = None
        row = self.avicultorRepository.getByIdAvicultor(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        if row is not None:
            id = row[0]
            nome = row[1]
            nascimento = row[2]
            cpf = row[3]
            caf = row[4]
            avicultor = Avicultor(id, nome, nascimento, cpf, caf)
        return avicultor