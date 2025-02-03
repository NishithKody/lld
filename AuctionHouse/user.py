from uuid import uuid4

class User:
    def __init__(self, name, email, password):
        self.id = uuid4()
        self.name = name
        self.email = email
        self.password = password
    
    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
    

    