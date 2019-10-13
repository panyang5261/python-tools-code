

class singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_state'):
            cls._state = super().__new__(cls, *args, **kwargs)
        return cls._state


class singleton2:
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj


def signleton3(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return inner


@signleton3
class A:
    pass




if __name__ == '__main__':
    s3 = A()
    s4 = A()
    print(s3 is s4)

    # s2 = singleton2()
    # print(id(s2))
    #
    # s3 = singleton2()
    # print(id(s3))
    #
    # s2 = singleton()
    # print(id(s2))
    #
    # s3 = singleton()
    # print(id(s3))