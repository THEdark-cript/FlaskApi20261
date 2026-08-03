from repositories.aviario_repository import AviarioRepository
from models.Aviario import AviarioSchema

class AviarioService:
    def __init__(self):
        self.repo = AviarioRepository()

    def listar(self):
        return self.repo.getAll()

    def buscar(self, id: int):
        return self.repo.getById(id)

    def criar(self, dados):
        schema = AviarioSchema()
        dados_validados = schema.load(dados)
        return self.repo.insert(dados_validados)

    def atualizar(self, id: int, dados):
        schema = AviarioSchema()
        dados_validados = schema.load(dados)
        return self.repo.update(id, dados_validados)

    def remover(self, id: int):
        return self.repo.delete(id)
