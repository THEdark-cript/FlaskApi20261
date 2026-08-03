import sqlite3
from flask import request
from helpers.application import app
from helpers.database import get_conn
from marshmallow import Schema, fields, validate

class Avicola:
    def __init__(self, id, nome, tipo, capacidade):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.capacidade = capacidade

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "capacidade": self.capacidade
        }
    
class AvicolaSchema(Schema):
    nome = fields.Str(required=True)
    tipo = fields.Str(required=True)
    capacidade = fields.Int(required=True, validate=validate.Range(min=1))   