
# importing the abc module
from abc import ABC, abstractmethod

# creating the class adding in a method
class Computer(ABC):
    @abstractmethod
    def Job(self):
        pass

    def anotherJob(self):
        print("I throw errors!")

    
# creating a child class and its method
class Laptop(Computer):
    def Job(self):
        print("I am a portable computer")
        
# creating a child class and its method
class Desktop(Computer):
    def Job(self):
        print("I stay put and compute")

# creating a child class, it's method calls on the parent class's method
class cellPhone(Computer):
    def Job(self):
        print("I do it all anywhere!")




#created objects
laptop = Laptop()
pc = Desktop()
cell = cellPhone()

#calling their functions
laptop.Job()
pc.Job()
cell.Job()


