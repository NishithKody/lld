from payment_interface import Payment

class CardPayment(Payment):
    def pay(self,amt):
        print("payment via card")
        return True