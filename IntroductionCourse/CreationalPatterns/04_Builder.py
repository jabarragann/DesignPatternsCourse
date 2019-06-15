class Director:

    def __init__(self, builder, cheapBuilder):
        self.__builder = builder
        self.__cheapBuilder = cheapBuilder

    def construct_car(self):
        self.__builder.create_new_car()
        self.__builder.add_model()
        self.__builder.add_tires()
        self.__builder.add_engine()

    def construct_cheap(self):
        self.__cheapBuilder.create_new_car()
        self.__cheapBuilder.add_model()
        self.__cheapBuilder.add_tires()
        self.__cheapBuilder.add_engine()

    def get_car(self):
        return self.__builder.car

    def get_cheap(self):
        return self.__cheapBuilder.car

class Builder:
    """Abstract Builder"""
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    """Concrete Builder ---> provides parts and tools to work on the parts"""
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"

class cheapBuilder(Builder):
    """Concrete Builder ---> provides parts and tools to work on the parts"""
    def add_model(self):
        self.car.model = "cheap"

    def add_tires(self):
        self.car.tires = "Cheap tires"

    def add_engine(self):
        self.car.engine = "Cheap engine"

class Car:
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine =None

    def __str__(self):
        return "{} | {} | {} ".format(self.model, self.tires, self.engine)



director = Director(SkyLarkBuilder(), cheapBuilder())

director.construct_car()
director.construct_cheap()
car1 = director.get_car()
car2 = director.get_cheap()

director.construct_car()
car3 = director.get_car()

print(car1)
print(car2)
print(car1 == car3)
print(id(car1))
print(id(car2))

