from . import base_table as bt

class Field:
    def __init__(self):
        self.name = None
    
    def set_name(self, name):
        self.name = name

    def check(self, value) -> bool:
        return True
    
    def new(self, value):
        if self.check(value):
            return value
        else:
            raise ValueError()
    
    def __repr__(self) -> str:
        return f'<Field named: {self.name}>'


class PrimaryKey(Field):
    def __init__(self, cls):
        super().__init__()
        self.name = 'id'
        self.supercls = cls


class ForeignKey:
    def __init__(self, table: 'bt.Table'):
        super().__init__()
        self.table = table 