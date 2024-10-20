from log_levels import LogLevels
from datetime import datetime

class Request:
    def __init__(self, level:LogLevels, msg:str) -> None:
        self.level = level
        self.msg = msg
        self.ts = datetime.now()

    def get_level(self):
        return self.level
    
    def get_msg(self):
        return self.msg
