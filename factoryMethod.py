class Vehicle:
    def drive(self):
        raise NotImplementedError("Base class should implement this")
    
class Car(Vehicle):
    def drive(self):
        print('car is running')

class Bike(Vehicle):
    def drive(self):
        print('bike is running')


class VehicleFactory:
    def create_vehicle(self, type) -> Vehicle:
        if(type == "car"):
            return Car()
        elif (type == "bike"):
            return Bike()
        else:
            raise ValueError("unknown type")

if(__name__ == "__main__"): # this is used to determine if the script is being run directly or being imported as a module in a another script
    factory = VehicleFactory()              # when the script is run, the special python variable __name__ is set to '__main__'
                                            # if it is imported, __name__ is set to the name of the module
    car = factory.create_vehicle('car')     # benefit
    car.drive()                             # this allows for a portion of the code to be run when the script is executed directly and not when it in imported
                                            # it is useful during testing or demo of the script 
    bike = factory.create_vehicle('bike')
    bike.drive()


# improvements 
# the VehicleFactory does not follow the open close principle
from abc import ABC, abstractmethod

class VehicleFactory2(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory2):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory2):
    def create_vehicle(self):
        return Bike()


if(__name__ == '__main__'):
    car_factory = CarFactory()
    car2 = car_factory.create_vehicle()
    car2.drive()