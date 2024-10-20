from abc import abstractmethod

class Payment():

    @abstractmethod
    def pay(self,amt):
        pass