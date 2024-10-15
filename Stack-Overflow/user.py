class User:
    def __init__(self,id:str, email:str, name:str) -> None:
        self.id = id
        self.email = email
        self.name = name
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
