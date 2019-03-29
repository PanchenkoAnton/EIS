STR_LEN = 13

class MyMetaClass(type):
    def __new__(cls, name, bases, dct):
        dct['COLLECTION'] = name.capitalize()
        #return type.__new__(cls, name, bases, dct)
        return super(MyMetaClass, cls).__new__(cls, name, bases, dct)

class Account:
    __metaclass__ = MyMetaClass
    def __init__(self):
        self._str_attr = None
    @property
    def str_attr(self):
        return self._str_attr
    @str_attr.setter
    def str_attr(self, value):
        if len(value) != STR_LEN:
            raise ValueError('The string must be 13 characters long.')
        if not isinstance(value, str):
            raise ValueError('The input must be a string.')
        self._str_attr = value


if __name__ == "__main__":
    myObject = Account()
    myObject.str_attr = '1234567890123'
    print(myObject._str_attr)
    #myObject.str_attr = '123'
    print(myObject._str_attr)
    #myObject.str_attr = '120329841027491749812'
    print(myObject._str_attr)
    #myObject.str_attr = ''
    print(myObject._str_attr)
    pass
