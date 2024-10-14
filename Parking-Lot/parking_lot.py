from level import Level
from vehicle import Vehicle
from typing import List

class Parking_lot:
    _instance = None

    def __init__(self) -> None:
        if(Parking_lot._instance is not None):
            raise Exception("Singleton")
        else:
            Parking_lot._instance = self
            self.levels: List[Level] = []
            # self.levels.append(Level(1,20))

    @staticmethod
    def get_instance():
        if(Parking_lot._instance is None):
            Parking_lot()
        
        return Parking_lot._instance
    
    def add_level(self, level:Level):
        self.levels.append(level)
    
    def park_vehicle(self, vehicle:Vehicle):
        for level in self.levels:
            if (level.park_vehicle(vehicle)):
                return True
        return False

    def unpark_vehicle(self, vehicle:Vehicle):
        for level in self.levels:
            if(level.unpark_vehicle(vehicle)):
                return True
        return False
    
    def display_avail(self):
        for level in self.levels:
            level.display_avai()