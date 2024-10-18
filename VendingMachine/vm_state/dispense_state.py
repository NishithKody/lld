from vm_state.state import State
from product import Product
from coins import Coin
from cash import Cash

class DispenseState(State):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine
        print('switch to dispense state')
    
    def select_product(self, product:Product):
        print('Please wait, a product is being dispensed')

    def insert_coin(self, coin:Coin):
        print('Please wait, a product is being dispensed')

    def insert_cash(self, cash:Cash):
        print('Please wait, a product is being dispensed')

    def dispense_product(self):
        print('Please wait, a product is being dispensed')

    def return_change(self):
        if(self.vending_machine.total_payment>self.vending_machine.selected_product.value):
            change= self.vending_machine.total_payment - self.vending_machine.selected_product.value
            print('returning change',change)
        else:
            print('no change to return')
        
        self.vending_machine.reset_product()
        self.vending_machine.reset_payment()
        self.vending_machine.set_state(self.vending_machine.idle_state)
