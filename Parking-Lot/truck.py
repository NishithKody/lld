from vehicle import Vehicle
from vechicle_type import VehicleType

class Truck(Vehicle):
    def __init__(self, ln_no:str)->None:
        super().__init__(VehicleType.CAR, ln_no)