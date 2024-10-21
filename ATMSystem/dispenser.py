
class Dispenser:
    def __init__(self, amt) -> None:
        self.amt = amt
    
    def get_total_amt(self):
        return self.amt

    def dispense_cash(self, value):
        print(' Dispensing cash ',value) #validations
        self.amt -= value
