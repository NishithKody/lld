from trx import Txn
from account import Account

class DepositTxn(Txn):
    def __init__(self, acc: Account, value) -> None:
        self.acc = acc
        self.value = value
    
    def excute(self):
        self.acc.credit(self.value)
