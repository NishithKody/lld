
class Account:
    def __init__(self, acc_no, initial_bal) -> None:
        self.acc_no = acc_no
        self.bal = initial_bal
    
    def get_acc_no(self):
        return self.acc_no
    
    def get_bal(self):
        return self.bal

    def credit(self, value):
        self.bal += value
    
    def debit(self, value):
        self.bal -= value
    