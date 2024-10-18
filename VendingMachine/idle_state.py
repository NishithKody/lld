from state import State
from product import Product
from coins import Coin
from cash import Cash

class IdleState(State):
    def __init__(self, vending_machine) -> None:
        self.vending_machine = vending_machine
    
    def select_product(self, product:Product):
        if(self.vending_machine.inventory.is_avail(product)):
            print('product selected',product.name)
            self.vending_machine.selected_product = product
            self.vending_machine.set_state(self.vending_machine.ready_state)
        else:
            print('product is not avail')

    def insert_coin(self, coin:Coin):
        print('please select product')

    def insert_cash(self, cash:Cash):
        print('please select product')

    def dispense_product(self):
        print('please select product')

    def return_change(self):
        print('please select product')


    