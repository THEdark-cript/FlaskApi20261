from marshmallow import Schema, fields, validate

class Galpao:
    def __init__(self, id, nome, capacidade, tipo):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade
        self.tipo = tipo

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "capacidade": self.capacidade,
            "tipo": self.tipo
        }

class GalpaoSchema(Schema):
    nome = fields.Str(required=True)
    capacidade = fields.Int(required=True, validate=validate.Range(min=1))
    tipo = fields.Str(required=True)
