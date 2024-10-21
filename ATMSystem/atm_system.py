from banking_service import BankingService
from withdraw_txn import WithdrawTxn
from deposit_txn import DepositTxn
from dispenser import Dispenser

class ATMSystem:
    def __init__(self, dispenser: Dispenser, banking_service: BankingService) -> None:
        self.banking_service = banking_service
        self.dispenser = dispenser
    
    def verify_card(self, card_id, pin):
        pass
    
    #bal enquiry
    def bal_enquiry(self, acc_id):
        acc = self.banking_service.get_acc(acc_id)
        return acc.get_bal()

    def withdraw(self, acc_id, value):
        pass

    def deposit(self, acc_id, value):
        pass


