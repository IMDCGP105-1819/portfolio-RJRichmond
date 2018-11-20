class Car(object):
    def __init__(self,manu,model,colour,doors):
        self.manu = manu;
        self.model = model;
        self.colour = colour;
        self.doors = doors;
    def __str__(self):
        return str("The car is a "+self.manu+", its a model "+self.model+", its colour is "+self.colour+" and it has "+str(self.doors)+" doors!")

    def CarColour(self, colour):
        self.colour = colour
    def CarManu(self,manu):
        self.manu = manu
    def CarModel(self,model):
        self.model = model
    def CarDoors(self,doors):
        self.doors = doors
CarDescription = Car("Aston Martin","DB12","Silver",2)
CarDescription.CarColour("Yellow")
CarDescription.CarManu("Reliant")
CarDescription.CarModel("Rialto GLS 2")
CarDescription.CarDoors(2)
print(CarDescription)
