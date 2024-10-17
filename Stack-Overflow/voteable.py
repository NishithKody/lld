from abc import abstractmethod

class Voteable:
    
    @abstractmethod
    def vote(self,user,value):
        return
    
    @abstractmethod
    def get_vote_count(self):
        pass