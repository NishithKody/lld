import uuid 

class Comment:
    def __init__(self,author,content) -> None:
        self.id = str(uuid.uuid4())
        self.author= author
        self.content = content
