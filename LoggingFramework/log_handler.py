from abc import abstractmethod

class LogHandler():
    @abstractmethod
    def handle_request(self, req):
        pass
