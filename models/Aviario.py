import sqlite3
from flask import request
from helpers.application import app
from helpers.database import get_conn
from marshmallow import Schema, fields, validate

class Aviario:
    def __init__(self, id, nome, localizacao, capacidade):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.capacidade = capacidade

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "localizacao": self.localizacao,
            "capacidade": self.capacidade
        }

class AviarioSchema(Schema):
    nome = fields.Str(required=True)
    localizacao = fields.Str(required=True)
    capacidade = fields.Int(required=True, validate=validate.Range(min=1))