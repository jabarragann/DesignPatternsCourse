
"""
Example of how to use class variables and "private" instance variables in python.

https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
"""
class Person:
    all_names = []
    __all_id = []

    def __init__(self, name, id = "secret"):
        self.name = name
        self.__private_id = id
        Person.all_names.append(name)
        Person.__all_id.append(id)

bob = Person("Bob")
mary = Person("Mary")
lily = Person("Lily")
print(Person.all_names)
print(mary.all_names)
print(Person.__dict__)
print(bob.__dict__)
print(bob._Person__private_id)

"""
How to create functions with variable arguments with *args and **kwargs
http://book.pythontips.com/en/latest/args_and_kwargs.html
"""
def func1(firstArg, *args):
    print("First arg: {}".format(firstArg))
    for ar in args:
        print("Additional {}".format(ar))

fruits = ['Banana','Strawberry', 'Pineapple']
func1("Hello My name is Juan", *fruits)

def func2(firstArg,**kwargs):
    print("First arg: {}".format(firstArg))
    for key, value in kwargs.items():
        print('{} ==> {}'.format(key, value))

person = {'name':'juan','lastname':'barragan'}
person.update(age = 18, favoriteBook = 'The art of learning')
func2('yolooo!', **person)

"""
Pointers in Python my own example
"""
dict1 = {"food":"Pasta"}
dict2 = dict1

dict2.update(beverage="Water")
print(dict1)
print(dict2)

"""
Singleton Example
"""

class Borg:
    """Borg class making class attributes global"""
    """Private global State dict"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def getShareState(self):
        return Borg.__shared_state

class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #self.__shared_state.update(kwargs)
        #self._Borg__shared_state.update(kwargs)
        self.__dict__.update(kwargs)

    def __str__(self):
        #return str(self.__shared_state)
        #return str(self._Borg__shared_state)
        return str(self.__dict__)


#Example of use
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)
y = Singleton(SNMP = "Simple Network Management Protocol")
print(str(y.getShareState()))

# person = {'name':'juan','lastname':'barragan'}
# y.__dict__ = person
# print(y.name)
# print(y.__dict__)
# print(Borg.__dict__)



