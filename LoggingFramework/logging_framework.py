from error_log import ErrorLog
from warning_log import WarningLog

class LoggingFramwork:
    _instance = None

    def __init__(self) -> None:
        if(LoggingFramwork._instance is not None):
            raise Exception("singleton")
        else:
            LoggingFramwork._instance = self
            self.error_level = ErrorLog(None)
            self.warning_level = WarningLog(self.error_level)

    @staticmethod
    def get_instance():
        if(LoggingFramwork._instance is None):
            LoggingFramwork()
        return LoggingFramwork._instance

    def handle(self,req):
        self.warning_level.handle_request(req)
