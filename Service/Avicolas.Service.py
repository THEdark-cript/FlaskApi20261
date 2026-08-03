from repositories.avicola_repository import AvicolaRepository
from models.Avicola import AvicolaSchema, Avicola

class AvicolaService():
    def getAvicola(self, id):
        row = AvicolaRepository().getByIdAvicola(id)
        return Avicola(*row) if row else None

    def getAvicolas(self):
        rows = AvicolaRepository().getAllAvicolas()
        return [Avicola(*row) for row in rows]

    def criarAvicola(self, dados):
        schema = AvicolaSchema()
        dados_validados = schema.load(dados)
        return AvicolaRepository().insertAvicola(dados_validados)

    def atualizarAvicola(self, id, dados):
        schema = AvicolaSchema()
        dados_validados = schema.load(dados)
        return AvicolaRepository().updateAvicola(id, dados_validados)

    def removerAvicola(self, id):
        return AvicolaRepository().deleteAvicola(id)
