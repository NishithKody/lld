from abc import ABC, abstractmethod

class State:
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def review_cart(self):
        pass

    @abstractmethod
    def checkout_cart(self):
        pass

class EmptyCartState(State):

    def add_item(self, item):
        print('item has been added')
        return AdditemToCart()
    
    def review_cart(self):
        print('cant review empty cart')
        return self
    
    def checkout_cart(self):
        print('cant checkout empty cart')
        return self

class AdditemToCart(State):
    
    def add_item(self, item):
        print('item has been added ')
        return self

    def review_cart(self):
        print('reviewing the cart')
        return ReviewCart()
    
    def checkout_cart(self):
        print("need to first review the cart")
        return self

class ReviewCart(State):
    def add_item(self, item):
        print("item has been added")
        return AdditemToCart()
    
    def review_cart(self):
        print('reviewing the cart')
        return self
    
    def checkout_cart(self):
        print('checkout cart')
        return CheckoutCart()

class CheckoutCart(State):
    def add_item(self, item):
        print('Cant add items during checkout')
        return self
    
    def review_cart(self):
        print('reviewing the cart')
        return ReviewCart()
    
    def checkout_cart(self):
        print('Checking out the cart')
        return self

class Context:
    def __init__(self):
        self.current_state = EmptyCartState()
    
    def add_item(self,item):
        self.current_state = self.current_state.add_item(item)
    
    def review_cart(self):
        self.current_state = self.current_state.review_cart()
    
    def checkout_cart(self):
        self.current_state = self.current_state.checkout_cart()


def Client():
    context = Context()

    context.add_item('tool')
    context.review_cart()
    context.checkout_cart()

    print('-----------------')

    context.add_item('tool')
    context.checkout_cart()
    context.review_cart()
    


if(__name__=='__main__'):
    Client()