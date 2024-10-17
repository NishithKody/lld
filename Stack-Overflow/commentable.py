from abc import abstractmethod

class Commentable:
    @abstractmethod
    def add_comment(self,comment):
        pass

    @abstractmethod
    def get_comment(self):
        pass