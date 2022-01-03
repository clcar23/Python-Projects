
# creating the class
class Protected:
    def __init__(self):
        #leaving the name blank for now
        self.protectedName = ""
#creating obj variable for the class above
obj = Protected()
#passing in the name 'Dexter'
obj._protectedName = "Dexter"
#printing out our protected name
print(obj._protectedName)

# creating the class
class Protected2:
    def __init__(self):
        # setting the privateStr var to a string
        self.__privateStr = "I'm a chicken"

    # creating a child class of Protected2
    def getPrivate(self):
        # having it print our private string
        print(self.__privateStr)

    # creating another child class
    def setPrivate(self, private):
        # changing the name of the variable
        self.__privateStr = private

# creating obj variable for the parent class
obj = Protected2()
# calling our function getPrivate so it will print the string
obj.getPrivate()
# resetting the string 
obj.setPrivate("What are you")
 # calling the renamed string 
obj.getPrivate()
