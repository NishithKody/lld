from log_handler import LogHandler
from request import Request
from log_levels import LogLevels

class WarningLog(LogHandler):
    def __init__(self, next_handler) -> None:
        self.next_handler = next_handler
    
    def handle_request(self, req:Request):
        if(req.level == LogLevels.WARNING):
            print('warning-',req.msg)
        else:
            if(self.next_handler is not None):
                self.next_handler.handle_request(req)
