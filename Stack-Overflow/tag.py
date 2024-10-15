import uuid

class Tag:
    def __init__(self, name) -> None:
        self.id = str(uuid.uuid4())
        self.name = name