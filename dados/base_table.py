from . import fields
from . import manager
from typing import Any


class MetaTable(type):
    def __new__(cls, name: str, bases: tuple, namespace: 'dict[str, fields.Field | Any]'):
        _fields = {'id': fields.PrimaryKey(cls)}
        _header: 'list[str]' = ['id']

        for key, value in namespace.items():
            if isinstance(value, fields.Field):
                value.set_name(key)
                _fields.setdefault(key, value)
                _header.append(key)

        print(f'{name=}')
        print(f'{_fields=}')
        print(f'{_header=}')
        
        namespace.setdefault('_fields', _fields)
        namespace.setdefault('_header', _header)

        return type.__new__(cls, name, bases, namespace)


class Table(metaclass=MetaTable):
    regs: 'list[Table]' = []
    next_free_id = 0
    free_ids = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            f: fields.Field = self._fields.get(key, ValueError)

            if f == ValueError:
                raise f('Campo inexistente')
            
            setattr(self, key, f.new(value))

        for key in self._fields.keys():
            self.__dict__.setdefault(key, None)
        
        self.id = self.__class__.new_id()

        print('Objeto Criado com Sucesso')

        self.add()
        self.stage = {}
    
    @classmethod
    def init_from_db(cls, **kwargs):
        instance = cls.__new__(cls)
        instance.__dict__.update(kwargs)

        instance.add()
        instance.stage = {}

        return instance

    def __init_subclass__(cls, **kwargs):
        cls.regs: 'list[cls]' = []


    # MÉTODOS DE CLASSE ---

    @classmethod
    def get_header(cls) -> 'tuple[str]':
        return cls._header

    @classmethod
    def get_elements(cls) -> 'tuple[Table]':
        return tuple(cls.regs)
    
    @classmethod
    def filter_by(cls, **kwargs) -> 'list[Table]':
        regs = []
        
        for reg in cls.regs:
            for field, value in kwargs.items():
                if reg.get_value(field) != value:
                    break
            else:
                regs.append(reg)
        
        return regs
    
    @classmethod
    def get_by_pk(cls, value) -> 'Table':
        for reg in cls.regs:
            if getattr(reg, 'id') == value:
                return reg

    @classmethod
    def show_regs(cls):
        print(cls.regs)
    
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


    # MÉTODOS DE INSTÂNCIA ---

    def get_pk(self) -> int:
        return self.id
    
    def get_value(self, attr: str):
        try:
            return getattr(self, attr)
        except AttributeError:
            return None
    
    def get_all_values(self) -> tuple:
        return tuple(self.__dict__.values())
    
    def set_value(self, **kwargs):     
        for attr, value in kwargs.items():
            if self.get_value(attr) != None:
                setattr(self, attr, value)
    
    def add(self):
        self.__class__.regs.append(self)

    def save(self, commit=False) -> None:
        values = {}
        fields_names = self._fields.keys()

        for attr, val in self.__dict__.items():
            if attr in fields_names:
                values.setdefault(attr, val)

        print(f'{values=}')

        self.stage.update(values)
        
        if commit:
            result = manager.Manager.save_table(self.__class__)
            
            if result == ValueError:
                raise result

    
    def to_dict(self) -> dict:
        return self.stage