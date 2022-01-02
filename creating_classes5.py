
#defining the parent class
class Beer:
    color = "unknown"
    alcohol_content = "unknown"

    
    def Ingredients(self):
        return "Barley, Malt, Hops, Yeast"

    def Effects(self):
        return "Makes you see ghosts!"

    
#adding in a method
    def getColor(self):
        print(self.color)


#adding in a child class
class Lager(Beer):
#inheriting attributes from the parent class and adding in 2 new
    taste = "Malty and delicious"
    color = "Amber"
    alcohol_content = "12.4%"
    name = "Ryan's Red"

        
#using polymorphism to change the parent function
    def Ingredients(self):
        return "Malt, Barley, an old boot"
        

#adding in a child class
class Porter(Beer):
#inheriting attributes from the parent class and adding in 2 new
    fiber_content = 50
    color = "Dark"
    alcohol_content = "14.0%"
    name = "Benjamin's Brew"

        
#using polymorphism to change the parent function
    def Effects(self):
        return "Get's you movin!"





if __name__ == "__main__":
    #instantiate the class objects and call on their methods
    beer = Beer()
    
#printing attributes from the Lager class
    lager = Lager()
    print(lager.name)
    print(lager.Ingredients())

#printing attributes for the Porter class
    porter = Porter()
    print(porter.name)
    print(porter.Effects())
