
#create parent class of Animal using '__init__' method
class Animal:
    def__init__(self, name, weight, height, odor):
        #attributes
        self.name = name
        self.weight = weight
        self.height = height
        self.odor = odor

#create a child class called Farm
class Farm(Animal):
    def __init__(self, sound, diet, use, shelter):
        #attributes
        self.diet = diet
        self.sound = sound
        self.use = use
        self.shelter = shelter

#create child class of Animal called Zoo
class Zoo(Animal):
    def__init__(self, sound, diet, danger_level, habitat ):
        #attributes
        self.sound = sound
        self.diet = diet
        self.danger_level = danger_level
        self.habitat = habitat
