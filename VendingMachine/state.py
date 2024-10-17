from abc import abstractmethod

class State:
    
    @abstractmethod
    def select_product(self, product):
        pass

    @abstractmethod
    def insert_coin(self, coint):
        pass

    @abstractmethod
    def insert_cash(self, cash):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def return_change(self):
        pass