from repositories.galpao_repository import GalpaoRepository
from models.Galpao import GalpaoSchema

class GalpaoService:
    def __init__(self):
        self.repo = GalpaoRepository()

    def listar(self):
        return self.repo.getAll()

    def buscar(self, id: int):
        return self.repo.getById(id)

    def criar(self, dados):
        schema = GalpaoSchema()
        dados_validados = schema.load(dados)
        return self.repo.insert(dados_validados)

    def atualizar(self, id: int, dados):
        schema = GalpaoSchema()
        dados_validados = schema.load(dados)
        return self.repo.update(id, dados_validados)

    def remover(self, id: int):
        return self.repo.delete(id)
