from typing import Dict, List
from product import Product
from inventory import Inventory
from vm_state.state import State
from vm_state.idle_state import IdleState
from vm_state.ready_state import ReadyState
from coins import Coin
from cash import Cash

class VendingMachine:
    _instance = None

    def __init__(self) -> None:
        if(VendingMachine._instance is not None):
            raise Exception('The instance is present')
        else:
            VendingMachine._instance = self
            self.inventory = Inventory()
            self.selected_product = None
            self.total_payment = 0
            self.idle_state = IdleState(self)
            self.ready_state = ReadyState(self)
            self.current_state = self.idle_state

    @staticmethod
    def get_instance():
        if(VendingMachine._instance == None):
            VendingMachine()
        return VendingMachine._instance

    def set_state(self, state: State):
        self.current_state = state

    def select_product(self, product):
        self.current_state.select_product(product)
    
    def add_coin(self, coin:Coin):
        self.total_payment += coin.value
    
    def add_cash(self, cash:Cash):
        self.total_payment += cash.value
    
    def reset_product(self):
        self.selected_product = None
    
    def reset_payment(self):
        self.total_payment = 0


