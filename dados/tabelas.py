from . import base_table as bt
from . import fields
from . import setter as st


class Avaliacao(bt.Table):
    num_AV = fields.Field()
    nota = fields.Field()
    data = fields.Field()    

    def __repr__(self):
        return f'Avaliacao(Num_AV = {self.Num_AV}, Materia = {self.Materia})'


class Materia(bt.Table):
    nome = fields.Field()
    prof = fields.Field()
    dias = fields.Field()
    avaliacoes = fields.ForeignKey(Avaliacao)
    
    def __repr__(self):
        return f'Materia(Nome = {self.Nome}, Avaliacoes = {self.Avaliacoes})'


class A(bt.Table):
    num_av = fields.Field()
    data = fields.Field()
    pass


if __name__ == '__main__':

    avaliacao_data = st.load('Avaliacao')['values']
    materia_data = st.load('Materia')['values']

    a1 = Avaliacao(**avaliacao_data[0])
    a2 = Avaliacao(**avaliacao_data[1])

    m1 = Materia(**materia_data[1])
    m2 = Materia(**materia_data[2])

    Avaliacao.show_regs()
    Materia.show_regs()


