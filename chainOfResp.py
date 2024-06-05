from abc import ABC, abstractmethod

class Handler:
    @abstractmethod
    def handle_request(self,req):
        pass

class L1Support(Handler):
    def __init__(self, handler:Handler):
        self.handler = handler
    
    def handle_request(self, req):
        if(req=='1'):
            print("The request is level 1, L1 support will handle it")
        else:
            if self.handler is not None:
                self.handler.handle_request(req)

class L2Support(Handler):
    def __init__(self, handler:Handler):
        self.handler = handler
    
    def handle_request(self, req):
        if(req=='2'):
            print("The request is level 2, L2 support will handle it")
        else:
            if self.handler is not None:
                self.handler.handle_request(req)

class L3Support(Handler):
    def __init__(self, handler:Handler):
        self.handler = handler
    
    def handle_request(self, req):
        if(req=='3'):
            print("The request is level 3, L3 support will handle it")
        else:
            if self.handler is not None:
                self.handler.handle_request(req)

def Client(req):
    L3 = L3Support(None)
    L2 = L2Support(L3)
    L1 = L1Support(L2)

    L1.handle_request(req)

if(__name__=='__main__'):
    req = '3'
    Client(req)