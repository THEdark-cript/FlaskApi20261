from helpers.logger import logger
from Repository.AvicultorRepository import AvicultorRepository
from models.Avicultor import Avicultor

class AvicultorService():
    def __init__(self):
        self.avicultorRepository = AvicultorRepository()

    def getByIdAvicultor(self, id):
        row = self.avicultorRepository.getByIdAvicultor(id)
        logger.info("Service: Lendo informações do resultado da consulta ao banco.")
        if row is not None:
            return Avicultor(row[0], row[1], row[2], row[3], row[4])
        return None

    def getAllAvicultores(self):
        rows = self.avicultorRepository.getAll()
        avicultores = []
        for row in rows:
            avicultor = Avicultor(row[0], row[1], row[2], row[3], row[4])
            avicultores.append(avicultor.toDict())
        return avicultores

    def criarAvicultor(self, dados):
        self.avicultorRepository.insert(
            dados["nome"], str(dados["nascimento"]), dados["cpf"], dados["caf"]
        )
        return {"mensagem": "Avicultor criado com sucesso!"}

    def atualizarAvicultor(self, id, dados):
        linhas = self.avicultorRepository.update(
            id, dados["nome"], str(dados["nascimento"]), dados["cpf"], dados["caf"]
        )
        if linhas == 0:
            return None  
        return {"mensagem": "Avicultor atualizado com sucesso!"}

    def deletarAvicultor(self, id):
        logger.info(f"Service: Tentando deletar avicultor {id}.")
        existe = self.getByIdAvicultor(id)
        if not existe:
            return None
        self.avicultorRepository.delete(id)
        return {"mensagem": "Avicultor removido com sucesso!"}
