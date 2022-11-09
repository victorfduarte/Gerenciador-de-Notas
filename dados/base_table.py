
class TableClass:
    regs: 'list[TableClass]' = []
    next_free_id = 0
    free_ids = []

    def __init__(self, id: int):

        if id == None:
            self.ID = PrimaryKey(self, 'ID', self.__class__.new_id())
        else:
            self.ID = PrimaryKey(self, 'ID', self.__class__.new_id(id))

        self.add()
        self.PK = self.ID
        self.stage = {}

    def __init_subclass__(cls, **kwargs):
        cls.regs: 'list[cls]' = []

    @classmethod
    def get_header(cls) -> 'tuple[str]':
        pass

    @classmethod
    def get_elements(cls) -> 'tuple[TableClass]':
        return tuple(cls.regs)
    
    @classmethod
    def get_elements_by(cls, **kwargs) -> 'list[TableClass]':
        regs = []
        
        for reg in cls.regs:
            '''
            print([ord(c) for c in getattr(reg, field)])
            print([ord(c) for c in value])
            print(f'{getattr(reg, field)} - {value}')
            '''
            for field, value in kwargs.items():
                if reg.get_value(field).get() != value:
                    break
            else:
                regs.append(reg)
        
        return regs
    
    @classmethod
    def get_element_by_pk(cls, value) -> 'TableClass':
        for reg in cls.regs:
            if getattr(reg, 'PK') == value:
                return reg

    @classmethod
    def show_regs(cls):
        print(cls.regs)

    def add(self):
        self.__class__.regs.append(self)
    
    @classmethod
    def new_id(cls, default: int = None) -> int:
        if default == None:
            if cls.free_ids:
                return cls.free_ids.pop()

            new_id = cls.next_free_id
            cls.next_free_id += 1
            return new_id

        else:
            if default == cls.next_free_id:
                cls.next_free_id += 1
                return default
            
            if default > cls.next_free_id:
                cls.free_ids.extend(range(cls.next_free_id, default))
                cls.next_free_id = default + 1
                return default
            
            if default < cls.next_free_id:
                if default in cls.free_ids:
                    cls.free_ids.remove(default)
                    return default
                else:
                    raise ValueError('Este valor de para ID não pode ser utilizado')

    def get_pk(self) -> 'PrimaryKey':
        return self.PK
    
    def get_value(self, attr: str) -> 'Key | PrimaryKey | ForeignKey | None':
        try:
            return getattr(self, attr)
        except AttributeError:
            return None
    
    def get_all_values(self) -> tuple:
        pass

    def save(self, commit=False):
        pass
    
    def to_dict(self) -> dict:
        return self.stage

    def set_value(self, **kwargs):     
        for attr, value in kwargs.items():
            key = self.get_value(attr)
            if key != None:
                key.set(value)

class Key:
    def __init__(self, name: str, value):
        self.name = name
        self.value = value
    

    def set(self, value):
        self.value = value
    
    def set_name(self, name):
        self.name = name
    
    
    def get(self):
        return self.value
    
    def get_name(self):
        return self.name
    

    def __eq__(self, __obj):
        return self.value == __obj    

    def __str__(self):
        return str(self.value)


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
    
    def set_name(self, name: str):
        self.name = name
    
    def set_table(self, table: TableClass):
        self.table = table


    def get(self):
        return self.value
    
    def get_name(self):
        return self.name
    
    def get_table(self):
        return self.table

    
    def __eq__(self, __obj):
        return self.value == __obj 

    def __str__(self):
        return str(self.value)    