from state import State

class IdleState(State):
    def __init__(self, product) -> None:
        self.product = product
    
    
    