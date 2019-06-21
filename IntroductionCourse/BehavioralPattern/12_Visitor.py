class House(object):

    def __init__(self):
        electricityFix =False
        acFix = False

    def accept(self, visitor):

        """Interface to accept a visitor"""
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self,electrician):
        print(self, "worked on by", electrician)
        self.electricityFix = True

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):

    def visit(self, house):
        house.work_on_electricity(self)


hvac = HvacSpecialist()
electrician = Electrician()

house1 = House()

#Let the house accept a visit
house1.accept(hvac)
house1.accept(electrician)

print(house1.electricityFix)
