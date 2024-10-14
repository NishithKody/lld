from abc import abstractmethod
from vechicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_number) -> None:
        self.spot_number = spot_number
        self.type = VehicleType.CAR
        self.parked_vehicle = None
    
    def get_spot_number(self):
        return self.spot_number

    def get_vehicle_type(self):
        return self.type

    def get_vehicle(self):
        return self.parked_vehicle
    
    def is_available(self):
        if(self.parked_vehicle==None):
            return True
        else:
            return False
    
    def park_vehicle(self,vehicle: Vehicle):
        if(self.parked_vehicle==None and self.type==vehicle.type):
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or already occupied")
    
    def unpark(self):
        self.parked_vehicle = None
