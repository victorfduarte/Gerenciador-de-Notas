from . import base_table as bt
from . import fields


class Professor(bt.Table):
    nome = fields.Field()
    sobrenome = fields.Field()
    sexo = fields.Field()


class Telefone(bt.Table):
    cod_prof = fields.ForeignKey(Professor)
    telefone = fields.Field()


class Email(bt.Table):
    cod_prof = fields.ForeignKey(Professor)
    email = fields.Field()


class Materia(bt.Table):
    nome = fields.Field()
    prof = fields.ForeignKey(Professor)
    obs = fields.Field()
    
    def __repr__(self):
        return f'Materia(nome = {self.nome}, professor = {self.prof})'


class Avaliacao(bt.Table):
    nota = fields.Field()
    materia = fields.ForeignKey(Materia)
    data = fields.Field()
    tipo = fields.Field()
    peso = fields.Field()

    def __repr__(self):
        return f'Avaliacao(nota = {self.nota})'

