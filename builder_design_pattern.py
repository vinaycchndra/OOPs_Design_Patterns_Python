# Here we are creating a subway type burger where we have full control over the sauces and other materials 
# We have a burger which is having the protected member buns, patty, cheese whith different getter and setter methods
class Burger:
    
    def __init__(self):
        self.__buns = None
        self.__patty = None
        self.__cheese = None
    
    def setBuns(self, bunStyle):
        self.__buns = bunStyle
        
    def setPatty(self, patty):
        self.__patty = patty
        
    def setCheese(self, cheese):
        self.__cheese = cheese
        
    def getCheese(self):
        return self.__cheese
        
    def getPatty(self):
        return self.__patty
        
    def getBuns(self):
        return self.__buns
        


# Now we have a builder class which will build create the burger for us like factory however we have more control 
# the configuration of an object and we have different methods to create the objects for us. We could have given all the 
# inside the constructors of the Burger but that would have been very tightly coupled pattern 

class BurgerBuilder:
    
    def __init__(self):
        self.burger = Burger()
        
        
    def addBuns(self, bunStyle=None):
        if bunStyle is None:
            raise Exception('Please mention the bun type')
        self.burger.setBuns(bunStyle)
        return self
    
    def addPatty(self, pattyType=None):
        if pattyType is None:
            raise Exception('Please mention the patty type you want to use')
        self.burger.setPatty(pattyType)
        return self
        
    
    def addCheese(self, cheeseType=None):
        if cheeseType is None:
            raise Exception('Please mention the cheese type you want to use')
        self.burger.setCheese(cheeseType)
        return self
        
    def build(self):
        return self.burger
        
    
burger = BurgerBuilder().addBuns('Whole Wheet Bun').\
            addPatty('Potato Patty').\
            addCheese('American Patty').\
            build()
            
print('Your Burger Bun >>>>>', burger.getBuns())            
print('Cheese used in your burger  >>>>>', burger.getCheese())            
print('Patty in your burger >>>>>', burger.getPatty())

