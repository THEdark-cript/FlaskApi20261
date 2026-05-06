from wsgiref import validate

from marshmallow import Schema, fields

class Avicultor():
  def __init__(self, id, nome, nascimento, cpf, caf):
      self.id = id
      self.nome = nome
      self.nascimento = nascimento
      self.cpf = cpf
      self.caf = caf

  def toDict(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "nascimento": self.nascimento,
      "cpf": self.cpf,
      +"caf": self.caf
    }
  
  class Avicultorschema(schema):
     nome = fields.Str(required=true)
     nascimento = fields.Date(required=true)
     cpf = fields.Str(required=true, validate=validate.length(max=11))
     caf = fields.Str(required=true)