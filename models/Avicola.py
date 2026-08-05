from marshmallow import Schema, fields

class Avicola:
    def __init__(self, id, endereco, territorio):
        self.id = id
        self.endereco = endereco
        self.territorio = territorio

    def toDict(self):
        return {
            "id": self.id,
            "endereco": self.endereco,
            "territorio": self.territorio
        }

class AvicolaSchema(Schema):
    endereco = fields.Str(required=True)
    territorio = fields.Str(required=True)
