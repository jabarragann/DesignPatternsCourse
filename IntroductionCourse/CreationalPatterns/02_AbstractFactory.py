

class Dog:
    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"


class DogFactory:

    def get_pet(self):
        "Return a Dog object"
        return Dog()

    def get_food(self):
        "Return a Dog Food object"
        return "Dog Food!"

class PetStore:

    def __init__(self, pet_factory=None):
        "Pet_factory is our Abstract factory"
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Its food is '{}'".format(pet_food))



#Create a concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract factory
shop = PetStore(factory)

#Invoke the utility method to show details

shop.show_pet()

