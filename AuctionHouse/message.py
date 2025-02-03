from Interfaces.messageInterface import MessageInterface
from typing import List

class Message(MessageInterface):
    def __init__(self, message, tags:List=[]):
        self.message = message
        self.tags = tags
    
    def getMessage(self):
        return self.message

    def getTags(self):
        return self.tags
    