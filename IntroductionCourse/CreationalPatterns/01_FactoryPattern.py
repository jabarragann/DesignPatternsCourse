

class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"



def get_pet(pet='dog'):
    """The Factory method"""
    pets = dict(dog=Dog('Hope'), cat=Cat('Peace'))

    return pets[pet]


pet1 = get_pet('dog')
print(pet1.speak())

pet2 = get_pet('cat')
print(pet2.speak())