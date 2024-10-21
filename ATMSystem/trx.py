from abc import abstractmethod

class Txn:
    @abstractmethod
    def excute(self):
        pass
    