from uuid import uuid4
from AuctionHouse.Interfaces.messageInterface import MessageInterface
from typing import List

class User:
    def __init__(self, name, email, password):
        self.id = uuid4()
        self.name = name
        self.email = email
        self.password = password
        self.messages: List[MessageInterface] = []
    
    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
    
    def notifyUser(self, message: MessageInterface):
        self.messages.append(message)

    def getLatestmessage(self): 
        return self.messages.pop().getMessage()
    