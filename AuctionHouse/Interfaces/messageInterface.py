from abc import abstractmethod

class MessageInterface():

    @abstractmethod
    def getMessage(self):
        pass
    
    @abstractmethod
    def getTags(self):
        pass