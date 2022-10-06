class Singletone(type):
    '''
    Pattern, creating only one object of class
    and giving global access point to it
    '''
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singletone):
    '''
    Class - manager for work with Data Base
    '''
    def __init__(self):
        pass