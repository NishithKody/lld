from logging_framework import LoggingFramwork
from request import Request
from log_levels import LogLevels

class LogFrwDemo:
    def run(self):
        req1= Request(LogLevels.ERROR,"warning msg")
        logger = LoggingFramwork.get_instance()

        logger.handle(req1)

if(__name__=='__main__'):
    demo = LogFrwDemo()
    demo.run()


