from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass

class EmailStrategy(Strategy):
    def send_notification(self, message):
        print (f'Email: {message}')

class SmsStrategy(Strategy):
    def send_notification(self, message):
        print (f'SMS: {message}')

class Context():
    def __init__(self,strategy) -> None:
        self.strat = strategy
    
    def set_strategy(self,strategy):
        self.strat = strategy

    def execute_strategy(self,msg):
        self.strat.send_notification(msg)

if(__name__=='__main__'):
    emailStrategy = EmailStrategy()
    smsStrategy = SmsStrategy()

    context = Context(emailStrategy) #set default strategy if required
    context.execute_strategy('Notification update')

    context.set_strategy(smsStrategy)
    context.execute_strategy('Notification')

        