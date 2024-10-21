
class Card:
    def __init__(self, card_no, pin) -> None:
        self.card_no = card_no
        self.pin = pin
    
    def get_card_no(self):
        return self.card_no
    
    def get_pin(self):
        return self.pin
