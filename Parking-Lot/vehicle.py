from abc import abstractmethod
from vechicle_type import VehicleType

class Vehicle:
    def __init__(self, type:VehicleType, lnNo:str) -> None:
        self.type = type
        self.lnNo = lnNo
    
    def get_ln_no(self):
        return self.lnNo

    def get_type(self):
        return self.type