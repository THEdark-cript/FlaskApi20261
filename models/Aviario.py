from marshmallow import Schema, fields, validate

class Aviario:
    def __init__(self, id, nome, capacidade):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "capacidade": self.capacidade
        }

class AviarioSchema(Schema):
    nome = fields.Str(required=True)
    capacidade = fields.Int(required=True, validate=validate.Range(min=1))
