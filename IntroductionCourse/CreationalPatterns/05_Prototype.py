import copy

class Prototype:

    def __init__(self):
        self.__objects = {}
        self._test = None

    def register_object(self, name, obj):
        """Register an object"""
        self.__objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object """
        del self.__objects[name]

    def clone(self, prototype_name, **attr):
        """Clone a reistered object and update its attributes"""
        obj = copy.deepcopy(self.__objects.get(prototype_name))
        obj.__dict__.update(attr)
        return obj

class Car:

    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('car', c)

attr = {'name':'JuanCar','color':'blue','options':'turbo'}
c1 = prototype.clone('car', **attr)


print(c1)