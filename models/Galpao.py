import sqlite3
from flask import request
from helpers.application import app
from helpers.database import get_conn
from marshmallow import Schema, fields, validate

class Galpao:
    def __init__(self, id, nome, capacidade, avicola_id):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade
        self.avicola_id = avicola_id

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "capacidade": self.capacidade,
            "avicola_id": self.avicola_id
        }

class GalpaoSchema(Schema):
    nome = fields.Str(required=True)
    capacidade = fields.Int(required=True, validate=validate.Range(min=1))
    avicola_id = fields.Int(required=True)