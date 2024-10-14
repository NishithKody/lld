from vechicle_type import VehicleType
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, ln_no: str) -> None:
        super().__init__(VehicleType.CAR, ln_no)