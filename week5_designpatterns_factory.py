from abc import abstractmethod
from week5_designpatterns_singleton import PizzaSystemLogger

logger = PizzaSystemLogger()

class SidesFactory(object): 
    """ An factory class for side items """ 
    
    @classmethod 
    def create(cls, sideName, *args): 
        """ Factory method for creating an Sides instance """ 
        logger.__log__('Inside Create')

        sideName = sideName.lower().strip() 

        if sideName == 'breadsticks': 
            return Breadsticks(*args) 
        elif sideName == 'wings': 
            return Wings(*args) 
        elif sideName == 'knots': 
            return GarlicKnots(*args)
        elif sideName == 'fries': 
            return Fries(*args)

class Sides():

    def __init__(self, sideName):
        logger.__log__('Inside Sides init')
        self.sideName = sideName

    @ abstractmethod
    def getDefaultDippingSauce(self):
        pass 
    
    def __str__(self): 
        return "Class Name: {} - Side Name: {}".format(self.__class__.__name__, self.sideName)


class Breadsticks(Sides):
    """ A Breadsticks Side """

    def getDefaultDippingSauce(self):
        return "Marinara"

class Wings(Sides):
    """ A Wings Side """

    def getDefaultDippingSauce(self):
        return "Ranch"

class GarlicKnots(Sides):
    """ A Garlic Knots Side """

    def getDefaultDippingSauce(self):
        return "Garlic Butter"

class Fries(Sides):
    """ A Fries Side """

    def getDefaultDippingSauce(self):
        return "Ketchup"


factory = SidesFactory()
breadSticks = factory.create('breadsticks', 'breadsticks')
fries = factory.create('fries', 'fries')
garlicKnots = factory.create('knots', 'knots')
wings = factory.create('wings', 'wings')

print("*** These sides and dipping sauces are available ***")
print("{} - Dipping Sauce: {}".format(breadSticks, breadSticks.getDefaultDippingSauce())) 
print("{} - Dipping Sauce: {}".format(fries, fries.getDefaultDippingSauce())) 
print("{} - Dipping Sauce: {}".format(garlicKnots, garlicKnots.getDefaultDippingSauce())) 
print("{} - Dipping Sauce: {}".format(wings, wings.getDefaultDippingSauce())) 