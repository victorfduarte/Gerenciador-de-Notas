
class TableClass:
    regs: 'list[TableClass]' = []

    def __init__(self):
        self.add()
        self.PK = PrimaryKey(self, '', '')

    def __init_subclass__(cls, **kwargs):
        cls.regs: 'list[cls]' = []
    
    def add(self):
        self.__class__.regs.append(self)
    
    def new_id(self):
        pass

    def get_pk(self) -> 'PrimaryKey':
        return self.PK

    @classmethod
    def get_elements(cls) -> 'tuple[TableClass]':
        return tuple(cls.regs)
    
    @classmethod
    def get_elements_by(cls, field: str, value):
        regs = []
        
        for reg in cls.regs:
            '''
            print([ord(c) for c in getattr(reg, field)])
            print([ord(c) for c in value])
            print(f'{getattr(reg, field)} - {value}')
            '''
            if getattr(reg, field) == value:
                regs.append(reg)
        
        return regs
    
    @classmethod
    def get_element_pk(cls, value):
        for reg in cls.regs:
            if getattr(reg, 'PK') == value:
                return reg

    @classmethod
    def show_regs(cls):
        print(cls.regs)


class PrimaryKey:
    def __init__(self, register: TableClass, name: str, value):
        self.register = register
        self.name = name
        self.value = value

        setattr(register, 'PK', self)
    

    def set(self, value):
        self.value = value
    
    def set_name(self, name):
        self.name = name
    
    def set_register(self, register):
        self.register = register


    def get(self):
        return self.value
    
    def get_name(self):
        return self.name
    
    def get_register(self):
        return self.register


    def __eq__(self, __obj):
        return self.value == __obj    

    def __str__(self):
        return str(self.value)


class ForeignKey:
    def __init__(self, table: TableClass, name: str, value):
        self.table = table
        self.name = name
        self.value = value
    

    def set(self, value):
        self.value = value
    
    def set_name(self, name):
        self.name = name
    
    def set_table(self, table):
        self.table = table


    def get(self):
        return self.value
    
    def get_name(self):
        return self.name
    
    def get_table(self):
        return self.table
    

    def __str__(self):
        return str(self.value)    