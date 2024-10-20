from uuid import uuid4
class Car:
    def __init__(self, make, model, price, plate) -> None:
        self.id = str(uuid4())
        self.make = make
        self.model = model
        self.price = price
        self.plate = plate
        self.isReserved = False
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def get_plate(self):
        return self.get_plate

    def is_avail(self):
        return self.isReserved
    
    def set_avail(self, avail):
        self.is_avail = avail
    
