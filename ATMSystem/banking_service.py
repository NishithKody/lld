from account import Account
class BankingService:
    def __init__(self) -> None:
        self.accounts = {}
    
    def add_acc(self, acc_no, amt):
        self.accounts[acc_no] = Account(acc_no, amt)
    
    def get_acc(self, acc_no) -> Account:
        return self.accounts.get(acc_no)
    
    def execute(self, txn):
        txn.excute()
